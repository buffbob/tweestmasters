from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, session
from tweestmaster import db
from tweestmaster.forums.forms import ForumForm
from tweestmaster.models import Forum
from flask_login import current_user, login_required

forums = Blueprint('forums', __name__)

@forums.route("/forums/", methods=['GET', 'POST'])
@login_required
def all_forums():

    forums = Forum.query.all()
    arg_dict={
        "title":"Forums",
        "legend": "All Forum",
        "forums":forums
    }
    return render_template('forums/index.html', data=arg_dict)


@forums.route("/forums/new", methods=['GET', 'POST'])
@login_required
def new():
    #todo: neeed to denote forum and article? like in other pages
    form = ForumForm()
    # need to get articles and forum data
    #get from current articles
    if form.validate_on_submit():
        forum = Forum(name=form.name.data, leader_id=session.get("current_user_id, 0"),
                      description=form.description.data, picture=form.picture.data, is_public=form.is_public.data, password=form.password.data)
        db.session.add(forum)
        forum.users.append(current_user)
        db.session.commit()
        flash('Your Forum has been created!', 'success')
        return redirect(url_for('main.home'))
    arg_dict={
        "title":'New Forum',
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
    arg_dict= {
        "current_article": session.get('current_article_id', 1),  # default 1st article for display always
        "current_user": session.get("current_user_id", -1),  # -1 is unkwown user
        "current_forum_id": session.get('current_forum_id', 1),
        "id":id,
        "forum":forum,
        "current_forum_name":forum.name,
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
