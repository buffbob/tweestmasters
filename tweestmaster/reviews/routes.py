from flask import Blueprint, render_template
from flask_login import login_required, current_user


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
    arg_dict = {

    }
    return render_template("reviews/new_review.html", id=id)


def edit_review(id):
    # id is the review.id
    arg_dic = {

    }
    return render_template("reviews/<int:id>/edit", id=id)