from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, session
from tweestmaster import db
from tweestmaster.tweests.forms import TweestForm
from tweestmaster.models import Tweest,Article,ArticlePicture,User,Forum
from flask_login import current_user, login_required
from datetime import datetime
tweests = Blueprint('tweests', __name__)

@tweests.route("/tweests/new/<int:article_id>", methods=['GET', 'POST'])
@login_required
def new_tweest(article_id):
    form = TweestForm()
    cfn = Forum.query.filter_by(id=session.get('current_forum_id',1)).first().name
    cun = User.query.filter_by(id=session["current_user_id"]).first().username
    correct_content = ""
# todo: do we need this check :: send article_id with data
    #article_id = request.args.get("article_id")
    #if not article_id:
     #   arts = Article.query.all()

    article = Article.query.filter_by(id=article_id).first()

    forum_id = article.forum_id
    image = article.pics[0]
    #article = Article.query.filter_by(id=int(article_id)).first()
    #forum_id = article.forum_id
    # need to get articles and forum data
    #get from current articles
    if form.validate_on_submit():
        if form.content1.data and form.content2.data:
            flash("Question do you want to submit the pasted in content or the file you selected?", "danger")
            return redirect(url_for('tweests.new_tweest', article_id=article_id))
        elif form.content1.data:
            correct_content = form.content1.data
        elif form.content2.data:
            correct_content = form.content2.data
        else:
            #
            flash("You must paste in your tweesst or choose a file", "danger")
# todo: did danger work helppp 1/16?
            return redirect(url_for('tweests.new_tweest', article_id=article_id))

        tweest = Tweest(title=form.title.data, user_id=current_user.id,
                      content=correct_content, forum_id=forum_id,
                      article_id=article_id)
        db.session.add(tweest)
        db.session.commit()
        flash('Your Tweest has been created!', 'success')
        return redirect(url_for('main.home'))

    arg_dic = {
        "current_user_name":cun,
        "current_forum_name":cfn,
        "title":"New Tweest",
        "article_id":article_id,
        "article_title": article.title,
        "forum_id": forum_id,
        "article_content":article.content,
        "image": image,
        "legend": 'Create a new tweesst',
        "current_article": session.get('current_article', 1), # default 1st article for display always
        "current_user": session.get("current_user", -1), # -1 is unkwown user
        "current_forum": session.get('current_forum', 1), # master
    }

    return render_template('tweests/new.html', article_id=article_id, form=form, data=arg_dic)



def find_review_score(review):
    # review = row of review table
    return int((review.entertainment_score + review.style_score)/2)

@tweests.route("/tweest/<int:id>")
def tweest(id):
    """see helper method above"""
    #page = request.args.get('page', 1, type=int)# from query string
    tweest = Tweest.query.get_or_404(id) #
    tweests = Tweest.query.all()
    article_id=tweest.article_id
    #get reviews, feature article
    reviews =tweest.reviews
    reviews_authors_ids = None
    reviews_authors = None
    reviewed = False
    # todo: finish thought
    reviews_scores = [find_review_score(rev) for rev in reviews]
    print(f"length: {len(reviews)}")
    if reviews:
        reviews_authors_ids = [rev.user_id for rev in reviews]
        reviews_authors = [User.query.filter_by(id=auth_id).first().username for auth_id in reviews_authors_ids]
        if current_user.id in reviews_authors_ids:
            reviewed = True
        zipped = zip(reviews, reviews_authors, reviews_scores)
    else:
        zipped = None

    print(f"zipped = none is {zipped is None}")
    author_id = tweest.user_id
    author = User.query.filter_by(id=author_id).first()
    user_img = author.image_file
    post_date=tweest.date_created.strftime("%Y-%m-%d")
    dict_args = {
        "title":"Tweest",
        "tweest_title": tweest.title,
        "legend":"Booger",
        "tweest_id":id,
        'content': tweest.content,
        "author_image":user_img,
        "post_date":post_date,
        "article_id":article_id,
        "reviews_authors_scores":zipped,
        "not_reviewed": not reviewed,
    }
    print(f"length zipped: ")

    return render_template('tweests/tweest.html', id=id,  data=dict_args)


@tweests.route("/tweest/<int:tweest_id>/update", methods=['GET', 'POST'])
@login_required
def update_tweest(tweest_id):
    tweest = Tweest.query.get_or_404(tweest_id)
    if tweest.author != current_user.username:
        abort(403)
    form = TweestForm()
    if form.validate_on_submit():
        tweest.title = form.title.data
        tweest.content = form.content.data
        db.session.commit()
        flash('Your tweest has been updated!', 'success')
        return redirect(url_for('tweests.tweest', tweest_id=tweest.id))
    elif request.method == 'GET':
        form.title.data = tweest.title
        form.content.data = tweest.content
    return render_template('new.html', title='Update Tweest',
                           form=form, legend='Editing tweest')


@tweests.route("/tweests/<int:tweest_id>/delete", methods=['POST'])
@login_required
def delete_tweest(tweest_id):
    tweest = Tweest.query.get_or_404(tweest_id)
    if tweest.author != current_user:
        abort(403)
    db.session.delete(tweest)
    db.session.commit()
    flash('Your tweest has been deleted!', 'success')
    return redirect(url_for('main.home'))
