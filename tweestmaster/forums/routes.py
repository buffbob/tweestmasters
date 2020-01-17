from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
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
    form = ForumForm()
    # need to get articles and forum data
    #get from current articles
    if form.validate_on_submit():
        forum = Forum(name=form.name.data, leader_id=current_user.id,
                      description = form.description.data, picture=form.picture.data,
                      forum_type=form.forum_type.data)
        db.session.add(forum)
        forum.users.append(current_user)
        db.session.commit()
        flash('Your Forum has been created!', 'success')
        return redirect(url_for('main.home'))
    arg_dict={
        "title":'New Forum',
        'legend': 'Start a new Forum',
        "leader_id": current_user.id
    }
    return render_template('forums/new.html', form=form, data=arg_dict)



@forums.route("/forums/<int:id>")
def show(id):
    forum = Forum.query.get_or_404(id)
    arg_dict= {
        "id":id,
        "forum":forum,
        "title":forum.name,
        'legend':'start a new forum'
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
