import os
import json

app_name = "tweestmasters"
root_dir = "/etc/web_app_configs"
file_name = "config." + app_name + ".json"
file_path = root_dir + "/" + file_name

temp_1 = " "
temp_2 = " "
temp_3 = " "
temp_4 = " "

if os.path.isfile(file_path):
    with open(file_path) as file_config:
        config = json.load(file_config)
    temp_1 = config.get("SECRET_KEY")
    temp_2 = config.get("SQLALCHEMY_DATABASE_URI")
    temp_3 = config.get("EMAIL_USERNAME")
    temp_4 = config.get("EMAIL_PASS")

else:
    temp_1 = '4fb766da1c040c452e02703a752d233f'
    # temp_2 = 'sqlite:///site.db'
    temp_2 = 'mysql+pymysql://tweest:Root!@localhost:3306/tweestmasters'
    temp_3 = 'admin'
    temp_4 = 'email_password'


# sql settings
temp_5 = False
temp_6 = False


class Config:

    SECRET_KEY = temp_1
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = temp_2
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    MAIL_USERNAME = temp_3
    # MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = temp_4
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    SQLALCHEMY_ECHO = temp_5
    SQLALCHEMY_TRACK_MODIFICATIONS = temp_6

    # other config settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
