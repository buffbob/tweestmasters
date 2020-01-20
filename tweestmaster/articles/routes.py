from flask import session
from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from flask_login import current_user, login_required

from tweestmaster.models import User, Tweest, Article, Forum
from tweestmaster.articles.forms import ArticleForm, UpdateArticleForm
from tweestmaster.site_utils import format_and_save_article_pictures, send_reset_email
from tweestmaster import db, state
from tweestmaster.models import User, Tweest, Article, ArticlePicture
import os


articles = Blueprint('articles', __name__)


@articles.route("/article/<int:id>", methods=['GET', 'POST'])
@login_required
def article(id):
    article = Article.query.filter_by(id=id).first()
    user = User.query.filter_by(id=article.user_id).first()
    assert (article != False)
    f_id = article.forum_id
    current_forum = Forum.query.filter_by(id=f_id).first()
    current_forum_name = current_forum.name

    # tweests associated with this article
    tweests = article.tweests  # \
    # .order_by(Tweest.date_posted.desc())\
    # .paginate(page=page, per_page=5)
    # TODO: paginate, remove if block!!, tiny image etc.
    # image = glob.glob("static/feature_images/todays_images/*1.jpg")
    images = article.pics
    assert (len(images) >= 1)
    #TODO: DONT HARDCODE NEED TO BE SMART HERE
    path = "raven_tn.jpg"
    all_articles = Article.query.filter_by(forum_id=f_id) # all articles for a forum
    all_forums = Forum.query.all()


    user_ids = [tweest.user_id for tweest in tweests]
    user_names = [User.query.filter_by(id=each_id).first().username for each_id in user_ids]

    t_u = zip(tweests, user_ids, user_names)


    # image = tiny_image(image_file)
    # to be rendered in sidebar
    tweests_join = db.session.query(Tweest, User).filter(Tweest.article_id == id).all()
    data_args = {
        "tweests":tweests,
        "tweests_users":t_u,
        "id":id,
        "articles":all_articles,
        "forums":all_forums,
        "tweests_join":tweests_join,
        "images":images,
        "forum_id":f_id,
        "path":path,
        "article":article,
        "title":"Article",
        "legend": "an article by " + user.username,
        "current_article": session.get('current_article_id', 1),  # default 1st article for display always
        "current_user": session.get("current_user_id", -1),  # -1 is unkwown user
        "current_forum_id": session.get('current_forum_id', 1),  # master
        "current_forum_name":current_forum_name,
        "current_forum":current_forum,

    }
    return render_template('articles/article.html', id=id, data=data_args)


@articles.route("/article/<int:id>/edit", methods=['GET', 'POST'])
@login_required
def edit_article(id):
    form = UpdateArticleForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture = format_and_save_article_pictures(form.picture.data)
            current_user.image_file = picture
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('articles.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static/profile_pics/', filename=current_user.image_file)
    return render_template('articles/edit.html', title='Update Article',
                           image_file=image_file, form=form, id=id, legend='Update your article')


@login_required
@articles.route("/article/new", methods=['GET', 'POST'])
def new_article():
    form = ArticleForm()
    if request.method == "GET":
        return render_template('articles/new_article.html', title='New Article',
                               form=form, legend='Create a new article')
    if form.content1 and form.content2:
        flash("Question do you want to submit the pasted in content or the file you selected? Choose one only!", "success")
        return redirect(url_for('articles.new_article'))
    elif form.content1:
        correct_content_value = form.content1.data
    elif form.content2:
        correct_content_value = form.content2.data
    else:
        flash("You must paste in your article or choose a file", "danger")
        #todo: did danger work?
        return redirect(url_for('articles.new_article'))

    if form.validate_on_submit():
        forum = Forum.query.filter_by(name=state.get("forum")).first()
        pics = []
        #prepare list to format
        pics.append(form.pic1)  # this one is required
        if form.pic2:
            pics.append(form.pic2)
        if form.pic3:
            pics.append(form.pic3)
# now format and save pictures
        # I also need the tiny icon
        pic_names = format_and_save_article_pictures(pics)
        #icon will be a relative file path(string)
        #pic_names[0] should have a file in tiny for its icon
        icon = os.path.join(current_app.root_path, 'static/article_images/tiny', pic_names[0])
        article = Article(title=form.title.data, content=correct_content_value,
                          user_id=current_user.id, forum_id=forum.id, icon=icon)
        db.session.add(article)
        db.session.commit()
        article_id = Article.query.filter_by(title=form.title).first().id
  # a list of filename paths from root-directory
        for pic_name in pic_names:
            ArticlePicture(uri=pic_name, article_id=article_id)
        flash('Your article has been created!', 'success')

        #forums = current_user.forums #TODO ADD FORUMS SEE BELOW
        # return redirect(url_for('users.login'))
        return redirect(url_for('main.home'))
    # TODO: get all the forums/// a many to many relationship********************************
    # will be nice to get all the users of a forum too :/
    # using relationship table in sqlalchemy
    return render_template('articles/new_article.html', title='New Article', form=form, legend="Create New Article")
