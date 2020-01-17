from flask import render_template, request, Blueprint, session
from sqlalchemy import func

from tweestmaster.models import db, Tweest, Article, User, Forum

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home", methods=['GET','POST'])
def home():
    admin_id = 1 # admin
    current_article = Article.query.filter_by(user_id=admin_id).order_by(Article.user_id.desc()).first() # thus the newest article by admin
    article_id = current_article.id

    images = current_article.pics
    #tweests_users is tweest, user tuple
    tweests_users = db.session.query(Tweest, User).join(User).filter(Tweest.article_id == current_article.id).order_by(Tweest.id.asc()).all()
    #tweests = Tweest.query.filter(Tweest.article_id==feature_article.user_id).order_by(asc(Tweest.date_created)).all()
    #.paginate(page=page, per_page=5)
    # time to work on the feature articles

    all_articles = Article.query.order_by(Article.date_created.desc()).all()
    tweests_per_article = [len(e.tweests) for e in all_articles]
    sidebar_articles = zip(all_articles, tweests_per_article)

    session['current_user'] = -1 #unkown
    session['current_forum'] = 1 # master
    session['current_article'] = article_id
    arg_dic={
        "title":"Welcome",
        "article_id":article_id,
        "article_images":images,
        "article_content":current_article.content,
        "article_title":current_article.title,
        "tweests_users":tweests_users,
        "legend":"get started",
        "num_tweests":len(tweests_users),
        "sidebar_articles": sidebar_articles, # a tuple
        "sidebar_forums":"booger",
        "current_article": session.get('current_article', 1), # default 1st article for display always
        "current_user": session.get("current_user", -1), # -1 is unkwown user
        "current_forum": session.get('current_forum', 1), # master
    }
    return render_template('main/home.html', data=arg_dic)

@main.route("/how_to_get_started")
def get_started():
    arg_dic = {
        "title": "Getting Started",
    }
    return render_template("main/how_to_get_started.html", data = arg_dic)


@main.route("/fred", methods=['GET',"POST"])
def fred():
    a='shit'
    if request.method == "POST":
        a = request.form['gender']

    return render_template('fred.html',name=a)