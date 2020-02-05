from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#from flask_modus import Modus
#use this later during deployment
from tweestmaster.config import Config




state = {'forum': "Master"}

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


# modus = Modus(app)



def create_app():



    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config['SECRET_KEY'] = '4fb766da1c040c452e02703a752d233f'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config["SQLALCHEMY_ECHO"] = True
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    #modus = Modus(app)





    from tweestmaster.errors.handlers import errors
    from tweestmaster.tweests.routes import tweests
    from tweestmaster.main.routes import main
    from tweestmaster.articles.routes import articles
    from tweestmaster.forums.routes import forums
    from tweestmaster.reviews.routes import reviews

    from tweestmaster.users.routes import users

    app.register_blueprint(errors)
    app.register_blueprint(users)
    app.register_blueprint(tweests)
    app.register_blueprint(main)
    app.register_blueprint(articles)
    app.register_blueprint(forums)
    app.register_blueprint(reviews)

    return app