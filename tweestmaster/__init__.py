from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#from flask_modus import Modus
from tweestmaster.config import Config


app = Flask(__name__)
app.config['SECRET_KEY'] = '4fb766da1c040c452e02703a752d233f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)
#modus = Modus(app)

state = {'forum':"Master"}



from tweestmaster.errors.handlers import errors
from tweestmaster.tweests.routes import tweests
from tweestmaster.main.routes import main
from tweestmaster.articles.routes import articles
from tweestmaster.forums.routes import forums
from tweestmaster.reviews.routes import reviews

from tweestmaster.users.routes import users
from tweestmaster.site_utils import sql_debug


if app.debug:
    # app.after_request(sql_debug)
    pass


app.register_blueprint(errors)
app.register_blueprint(users)
app.register_blueprint(tweests)
app.register_blueprint(main)
app.register_blueprint(articles)
app.register_blueprint(forums)
app.register_blueprint(reviews)