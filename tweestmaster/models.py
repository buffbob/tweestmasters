from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from tweestmaster import db, login_manager
from flask_login import UserMixin, current_user
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


memberships = db.Table("memberships",
                       db.Column('forum_id', db.Integer, db.ForeignKey('forum.id'), primary_key=True),
                       db.Column("user_id", db.Integer, db.ForeignKey('user.id'), primary_key=True))
#Todo: add following capability(many to many) see
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='default.png')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # one to many relationships
    reviews = db.relationship("Review", backref="review_user", lazy=True)
    tweests = db.relationship("Tweest", backref='tweest_user', lazy=True)
    articles = db.relationship("Article", backref="article_user")
    # many to many---- must have the memberships table above to correlate
    forums = db.relationship("Forum", secondary="memberships", lazy='subquery',
                             backref=db.backref("users", lazy=True))

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.date_created})"

class Forum(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),  nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    picture = db.Column(db.String(100), nullable=False, default='site_images/default_landscape.jpg')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_private = db.Column(db.Boolean, nullable=False, default=False)
    # foreign key(s)
    leader_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # relationships
    articles = db.relationship("Article", backref='article_forum',lazy=True)
    tweests = db.relationship("Tweest", backref='tweest_forum', lazy=True)
    reviews = db.relationship("Review", backref="review_forum")


    def __repr__(self):
        return f"Forum({self.name}, {self.date_created})"  # , {self.leader_id})"


class Article(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    content = db.Column(db.String(10000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # foreign keys
    forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # relationships
    pics = db.relationship('ArticlePicture', backref='pic_article', lazy=True)
    sources = db.relationship("ArticleSource", backref="source_article", lazy=True)
    tweests = db.relationship("Tweest", backref="tweest_article", lazy=True)

    def __repr__(self):
        return f"Article({self.title}, {self.date_created}"


class ArticlePicture(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(100), nullable=False, default='default.png')
    # foreign key
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False)


# Articles can have sources
class ArticleSource(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    uri = db.Column(db.String(100), nullable=False)
    # foreign keys
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)

    def __repr__(self):
        return f""


# a response to an articles
class Tweest(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    content = db.Column(db.String(1000), nullable=False, unique=True)
    score = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, default=1)
    forum_id = db.Column(db.Integer, db.ForeignKey("forum.id"), nullable=False, default=1)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"), nullable=False, default=1)
    # relationship
    sources = db.relationship("tweestsource", backref='source_tweest', lazy=True)
    reviews = db.relationship("Review", backref="review_tweest", lazy=True)

    def __repr__(self):
        return f"Tweest({self.title})"

# tweests can have sources
class tweestsource(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    # foreign keys
    tweest_id = db.Column(db.Integer, db.ForeignKey('tweest.id'), nullable=False)


class Review(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    entertainment_score = db.Column(db.Integer, nullable=False),
    style_score = db.Column(db.Integer, nullable=False),
    content = db.Column(db.String(200),nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # foreign keys
    tweest_id = db.Column(db.Integer, db.ForeignKey('tweest.id'), nullable=False)
    forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

