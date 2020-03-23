from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from tweestmaster.models import Forum, Tweest, Article, User, Review
from tweestmaster.reviews.forms import ReviewForm
from tweestmaster import db

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
    if form.validate_on_submit():
        e_score = form.entertainment_score.data
        s_score = form.style_score.data
        local_avg_score = int((e_score + s_score)/2)
        review = Review(entertainment_score=e_score, style_score=s_score,
                        content=form.content.data, tweest_id=id,
                        user_id=current_user.id,
                        forum_id=tweestofconcern.forum_id)

        # update score for tweest of concern
        initial_score = tweestofconcern.score# score
        total_raw_score = 0
        if initial_score: ###### safer:::: >>  could also say if length of tweestofconcern.reviews == 0
            print(f"initial score of {initial_score}")
            revs = tweestofconcern.reviews
            num_reviews = len(revs)
            for rev in revs: # length or num reviews:
                temp = int((rev.entertainment_score + rev.style_score)/2)
                total_raw_score += temp

            new_score = (total_raw_score + local_avg_score)/(num_reviews+1)
        else:
            new_score = local_avg_score

        tweestofconcern.score = new_score
        db.session.add(review)
        db.session.commit()




    articleofconcern= Article.query.filter_by(id=tweestofconcern.article_id).first()
    forumofconcern = Forum.query.filter_by(id=session['current_forum_id']).first()

    tweest_author_id = tweestofconcern.user_id
    tweestofconcern_author = User.query.filter_by(id=tweest_author_id).first()
    author_name = tweestofconcern_author.username



    image = articleofconcern.pics[0]
    arg_dict = {
        "title":"Review",
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