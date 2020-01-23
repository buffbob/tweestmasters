from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from tweestmaster.models import Forum


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

    cfn = Forum.query.filter_by(id=session['current_forum_id']).first().name
    arg_dict = {
        "current_forum_name":cfn,
    }
    return render_template("reviews/new.html", id=id, data=arg_dict)


def edit_review(id):
    # id is the review.id
    arg_dic = {

    }
    return render_template("reviews/<int:id>/edit", id=id)