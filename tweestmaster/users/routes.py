from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app, session
from flask_login import login_user, current_user, logout_user, login_required
import os
from tweestmaster import db, bcrypt
from tweestmaster.models import User, Tweest, Article, Forum, Review
from tweestmaster.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from tweestmaster.site_utils import format_and_save_user_pic, send_reset_email

users = Blueprint('users', __name__)


@users.route("/new", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # noinspection PyArgumentList
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        #todo: add user to the Master forum
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        # return redirect(url_for('users.login'))
        return redirect(url_for('main.home'))
    arg_dict = {
        "title":"Register",
        "legend":"Register"
    }
    return render_template('users/new.html', form=form, data=arg_dict)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    arg_dict = {"title":"Login",
                "legend":"LOG IN"}
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # TODO: fix this password authentication
        if user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.user', id=user.id))
        elif user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')



    return render_template('users/login.html', data=arg_dict, form=form)


@users.route("/user/<int:id>", methods=['GET', 'POST'])
def user(id):
    huh = request.args
    sidebar_items=[]
    #articles,tweests,reviews are (each, user_of_interest) tuples
    person_of_interest = User.query.filter(User.id==id).first()
    articles = person_of_interest.articles
    tweests = person_of_interest.tweests
    # add the article picture for each tweest
    tweests_and_pics = [(tweest, Article.query.filter(Article.id==tweest.article_id).first().pics[0].uri) for tweest in tweests]
    reviews = person_of_interest.reviews
    forums = person_of_interest.forums

    # current forum name
    cfn = Forum.query.filter_by(id=session.get('current_forum_id',1)).first().name

    lena = len(articles)
    flag='booger'
    if lena > 0:
        # now a truple of (ariticle, user, image)
        article_pics = [a.pics[0] for a in articles]
        if article_pics:
            flag='article pics'
    else:
        article_pics = []
        flag='no pictures'

# use the lengths to display each respectively if necessary in html views
    lent = len(tweests)
    lenr = len(reviews)
    lenf = len(forums)
    lengths=(lena,lent,lenr,lenf)

    if request.method == "GET":   
        # sidebar_items is all_articles of all_forums
        all_articles = Article.query.order_by(Article.date_created.desc()).all()
        sidebar_items = all_articles
        #.order_by(Tweest.date_posted.desc())\
        #.paginate(page=page, per_page=5)
        # TODO: paginate, everything i need

    elif request.method =='POST':
        filter=request.form['radio']
        if filter == 'articles':
            all_articles = Article.query.order_by(Article.date_created.desc()).all()
            sidebar_items = all_articles
        elif filter == 'forums':
            all_forums = Forum.query.order_by(Forum.date_created.desc()).all()
            sidebar_items = all_forums
    # sidebar_items is variable to put in sidebar
    #image = tiny_image(image_file)
    path = os.path.join(current_app.root_path, "static/raven_tn.jpg")
    arg_dict = {
        #"title":current_user.username,
        'sidebar_data': sidebar_items,
        "forums":forums,
        "tweests_and_pics":tweests_and_pics,
        "articles":articles,
        "article_pics":article_pics,
        "reviews":reviews,
        "user_of_interst":current_user,
        "lengths":lengths,
        "flag":flag,
        "current_article":session.get('current_article_id'),
        "current_forum":session.get('current_forum_id'),
        "current_user":session.get("current_user_id"),
        "poi_date_joined":person_of_interest.date_created,
        "poi_username":person_of_interest.username,
        "current_forum_name":cfn,
    }
    return render_template('users/users.html', id=id, data=arg_dict)


@users.route("/users/<int:id>/edit", methods=['GET', 'POST'])
@login_required
def edit_account(id):
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture = format_and_save_user_pic(form.picture)
            current_user.image_file = picture
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('users/edit_account.html', title='Account',
                           image_file=image_file, form=form, id=id, legend="Edit account")


@users.route("/users/<int:id>/delete", methods=['GET', 'DELETE'])
@login_required
def delete_account(id):
    user = User.query.filter_by(id=id)
    if not user:
        return "no user found to delete"
    db.session.delete(user)
    db.session.commit()
# todo delete fix
    return ""


@users.route("/logout")
def logout():
    print('logout')
    logout_user()
    return redirect(url_for('main.home'))



@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form, legend="reset request")


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form, legend="reset token")

