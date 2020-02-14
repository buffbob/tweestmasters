from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, session
from tweestmaster import db
from tweestmaster.forums.forms import ForumForm
from tweestmaster.models import Forum, User, Article
from flask_login import current_user, login_required

forums = Blueprint('forums', __name__)


@forums.route("/forums/", methods=['GET', 'POST'])
def all_forums():
    forums = Forum.query.all()
    arg_dict = {
        "title": "Forums",
        "legend": "All Forum",
        "forums": forums
    }
    return render_template('forums/index.html', data=arg_dict)


@forums.route("/forums/new", methods=['GET', 'POST'])
@login_required
def new():
    # todo: neeed to denote forum and article? like in other pages
    # todo: nedd data['article-images']
    current_article = Article.query.filter_by(id=session.get("current_article_id")).order_by(Article.id.desc()).first()
    images = current_article.pics

    form = ForumForm()
    # need to get articles and forum data
    # get from current articles
    if form.validate_on_submit():
        forum = Forum(name=form.name.data, description=form.description.data,
                      is_private=form.is_private.data,
                      leader_id=session['current_user_id'])
        # could we use a ref to current_user.id
        # help!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # shall we create a membership-- yes
        db.session.add(forum)
        # add to the membership?
        forum.users.append(current_user)
        db.session.commit()
        flash('Your Forum has been created!', 'success')
        return redirect(url_for('main.home'))
    arg_dict = {
        "article_images": images,
        "title": 'New Forum',
        'legend': 'Start a new Forum',
        "leader_id": current_user.id,
        "current_article": session.get('current_article_id', 1),  # default 1st article for display always
        "current_user": session.get("current_user_id", 0),  # 0 is unkwown user
        "current_forum": session.get('current_forum_id', 1),  # master
    }
    return render_template('forums/new.html', form=form, data=arg_dict)


@forums.route("/forums/<int:id>")
def show(id):
    forum = Forum.query.get_or_404(id)
    just_joined = request.args.get('just_joined')
    # this is only difference when form(forum join button) is submited
    if just_joined == forum.name:
        # add user to forum
        forum.users.append(current_user)
        db.session.commit()
    session['current_forum_id'] = id
    forum = Forum.query.get_or_404(id)
    cun = "not logged in"
    if current_user.is_authenticated:
        cun = current_user.username
        cf_ids = [forum.id for forum in current_user.forums]
    else:
        cf_ids=[]
    a_member = (int(session.get("current_user_id")) in cf_ids)
    in_master = (forum.id == 1)

    art_authors = [User.query.filter_by(id=article.user_id).first().username for article in forum.articles]

    current_article = Article.query.filter_by(forum_id=id).order_by(Article.id.desc()).first()


    try:
        images = current_article.pics
        tweest_authors = [User.query.filter_by(id=each.user_id).first() for each in current_article.tweests]
        current_article_content = current_article.content
        current_article_title = current_article.title
        current_article_tweests = current_article.tweests

    except AttributeError as e:
        images = []
        tweest_authors = []
        current_article_title = ""
        current_article_content = ""
        current_article_tweests = []
        print(e)



    arg_dict = {
        "title":forum.name,
        "a_member":a_member,
        "in_master":in_master,
        "article_title": current_article_title,
        "article_content": current_article_content,
        "article_images": images,
        "current_user_name": cun,
        "current_article": session.get('current_article_id', 1),  # default 1st article for display always
        "current_user": session.get("current_user_id", -1),  # -1 is unkwown user
        "current_forum_id": session.get('current_forum_id', 1),
        "id": id,
        "forum": forum,
        "current_forum_name": forum.name,
        "articles": forum.articles,
        "z_art_authors": zip(forum.articles, art_authors),
        "tweests_tweest_authors": zip(current_article_tweests, tweest_authors)
    }
    return render_template('forums/show.html', data=arg_dict)


@forums.route("/forums/<int:id>/edit", methods=['GET', 'POST'])
@login_required
def edit(id):
    forum = Forum.query.get_or_404(id)
    if forum.leader_id != current_user.id:
        abort(403)
    form = ForumForm()
    if form.validate_on_submit():
        forum.name = form.name.data
        forum.description = form.description.data
        forum.leader_id = form.leader.data
        db.session.commit()
        flash('Your forum has been updated!', 'success')
        return redirect(url_for('forums.forum', tweest_id=forum.id))
    elif request.method == 'GET':
        form.name.data = forum.name
        form.content.data = forum.content
    return render_template('forums/edit.html', title='Update Forum',
                           form=form, legend='Updating forum!')


@forums.route("/forums/<int:id>/delete", methods=['POST'])
@login_required
def delete_forum(id):
    forum = Forum.query.get_or_404(id)
    if forum.author != current_user:
        abort(403)
    db.session.delete(forum)
    db.session.commit()
    flash('Your forum has been deleted!', 'success')
    return redirect(url_for('main.home'))
