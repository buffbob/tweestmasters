from PIL import Image
import os
import shutil
from datetime import datetime
from tweestmaster import mail,db
from flask import url_for, current_app
import secrets
from flask_mail import Message
from flask_sqlalchemy import get_debug_queries
from tweestmaster.models import User, Article, Tweest, Review


def sql_debug(response):
    queries = list(get_debug_queries())
    query_str = ""
    total_duration = 0.0
    for q in queries:
        total_duration+=q.duration
        stmt = str(q.statement %q.parameters).replace("\n",'\n    ')
        query_str += "Query: {0}\nDuration: {1}ms\n\n".format(stmt,round(q.duration * 1000, 2))
    print("="*80)
    print(' SQL Queries - {0} Queries Executed in {1}ms'.format(len(queries), round(total_duration * 1000, 2)))
    print('=' * 80)
    print(query_str.rstrip('\n'))
    print('=' * 80 + '\n')
    return response


def format_and_save_article_pictures(form_pictures):
    """
    hexs the filenames for uniqueness.
    formats pictures submitted to form and saves to appropriate folders
    once scaled.
    note that all files created will be strored in different directories
    but will have the same name-- making searching for them easier.)
    :param file: (list) the objects returned from form filefields
    :return: list of file paths for article image files
    """
    locations=[]

    sizes=[(700, 400), (200,130), (80,55)]
    for i, each in enumerate(form_pictures):
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(each.filename)
        picture_fn = random_hex + f_ext
        article_picture_path = os.path.join(current_app.root_path, 'static/article_images', picture_fn)
        locations.append(picture_fn)
        image = Image.open(each.data)
        # article size
        resized_image = image.resize(sizes[0], Image.ANTIALIAS)
        resized_image.save(article_picture_path)
        if i == 0:
            tiny_picture_path = os.path.join(current_app.root_path, 'static/article_images/tiny', picture_fn)
            super_tiny_picture_path = os.path.join(current_app.root_path, 'static/article_images/super_tiny', picture_fn)

            # tiny size
            resized_image = image.resize(sizes[1], Image.ANTIALIAS)
            resized_image.save(tiny_picture_path)
            # super tiny size
            resized_image = image.resize(sizes[2], Image.ANTIALIAS)
            resized_image.save(super_tiny_picture_path)
    return locations

def format_and_save_user_pic(filefield):
    """
    hexs the filenames for uniqueness.
    formats picture submitted to form and saves to appropriate folders
    once scaled.
    :param filefield: (FileField from form) the object returned from form filefield
    :return: the root file path of the image(a string). ex. booger.jpg
    """
    sizes = [(200,150), (50,50)]
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(filefield.data.filename)
    picture_fn = random_hex + f_ext
    user_picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    super_tiny_picture_path = os.path.join(current_app.root_path, 'static/profile_pics/super_tiny', picture_fn)

    image = Image.open(filefield.data)
    # avatar size
    resized_image = image.resize(sizes[0], Image.ANTIALIAS)
    resized_image.save(user_picture_path)
    # tiny size
    resized_image = image.resize(sizes[1], Image.ANTIALIAS)
    resized_image.save(super_tiny_picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
