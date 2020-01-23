from flask import render_template, request, Blueprint, session
from flask_login import current_user
from sqlalchemy import func

from tweestmaster.models import db, Tweest, Article, User, Forum

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home", methods=['GET','POST'])
def home():
    admin_id = 1 # admin
    initial_forum_id = 1 # master
    current_article = Article.query.filter_by(forum_id=initial_forum_id).order_by(Article.id.desc()).first() # thus the newest article by admin
    article_id = current_article.id
    cu=""
    # these 3 session variables are ints that are the id attribute of the current state.
    # this is used extensively in view functions.

    session['current_user_id'] = session.get("current_user_id", 0) # no current user
    session['current_forum_id'] = session.get("current_forum_id", 1)  # master
    session['current_article_id'] = article_id  # the id attribute of the feature article(int)


    images = current_article.pics
    #tweests_users is tweest, user tuple
    tweests_users = db.session.query(Tweest, User).join(User).filter(Tweest.article_id == article_id).order_by(Tweest.id.asc()).all()
    #tweests = Tweest.query.filter(Tweest.article_id==feature_article.user_id).order_by(asc(Tweest.date_created)).all()
    #.paginate(page=page, per_page=5)
    # time to work on the feature articles
    cfn = Forum.query.filter_by(id=session.get('current_forum_id',1)).first().name
    all_forums = Forum.query.all()
    # num tweests per Forum
    num_tweest_per_forum = [len(forum.tweests) for forum in all_forums]

    all_articles = Article.query.filter_by(forum_id=session['current_forum_id']).order_by(Article.date_created.desc()).all()
    tweests_per_article = [len(e.tweests) for e in all_articles]
    sidebar_articles = zip(all_articles, tweests_per_article)
    authors = [User.query.filter_by(id=article.user_id).first().username for article in all_articles]
    have_a_user = User.query.filter_by(id=session["current_user_id"]).first() is not None

    if have_a_user:
        cun = User.query.filter_by(id=session["current_user_id"]).first().username
    else:
        cun = "no current user"




    arg_dic={
        "cu":cu,
        "articles":all_articles,
        "article_authors":authors,
        "art_auth":zip(all_articles, authors, tweests_per_article), #
        "current_forum_name":cfn,
        "current_user_name":cun,
        "forums":all_forums,
        "filter":"articles",
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
        "current_article": session.get('current_article_id', 1), # default 1st article for display always
        "current_user": session.get("current_user_id", -1), # -1 is unkwown user
        "current_forum": session.get('current_forum_id', 1), # master
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