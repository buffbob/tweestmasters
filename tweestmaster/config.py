import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '4fb766da1c040c452e02703a752d233f'
    MAIL_USERNAME = 'lastgulch@gmail.com'
    MAIL_PASSWORD = "pass"
    # of course could use below
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SECRET_KEY = os.environ.get('MY_KEY')
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True