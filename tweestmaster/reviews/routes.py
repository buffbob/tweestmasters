from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from tweestmaster.models import Forum, Tweest, Article, User
from tweestmaster.reviews.forms import ReviewForm


reviews = Blueprint("reviews", __name__)


@reviews.route("/reviews/")
@login_required
def all_reviews():
    arg_dic = {

    }
    return render_template("reviews/reviews.html", data=arg_dic)

@reviews.route("/reviews/<int:id>")
@login_required
def review(id):
    # id is the review.id

    arg_dict={

    }
    return render_template("reviews/review.html", id=id, data=arg_dict)

@reviews.route("/reviews/new/<int:id>", methods=['GET', 'POST'])
@login_required
def new_review(id):
    # id is the tweest id
    form = ReviewForm()

    tweestofconcern = Tweest.query.filter_by(id=id).first()
    articleofconcern= Article.query.filter_by(id=tweestofconcern.article_id).first()
    forumofconcern = Forum.query.filter_by(id=session['current_forum_id']).first()

    tweest_author_id = tweestofconcern.user_id
    tweestofconcern_author = User.query.filter_by(id=tweest_author_id).first()
    author_name = tweestofconcern_author.username

    #article content, title
    # tweest title
    # tweest content

    image = articleofconcern.pics[0]
    arg_dict = {
        "image":image,
        "author_name":author_name,
        "article_content":articleofconcern.content,
        "article_title":articleofconcern.title,
        "article_images":articleofconcern.pics,
        "current_forum_name":forumofconcern.name,
        "tweest_title":tweestofconcern.title,
        "tweest_content":tweestofconcern.content,
        "current_article":articleofconcern.id
    }
    return render_template("reviews/new.html", form=form, data=arg_dict)


def edit_review(id):
    # id is the review.id
    arg_dic = {

    }
    return render_template("reviews/<int:id>/edit", id=id)