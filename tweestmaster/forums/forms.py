from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, FileField, IntegerField,BooleanField, TextAreaField,PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from tweestmaster.models import Forum


class ForumForm(FlaskForm):
    name = StringField('name your forum', validators=[DataRequired()])
    description = TextAreaField("give a short description of your forum", validators=[DataRequired()])
    theme = StringField("Theme?")
    picture = FileField("select a forum photo", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    is_private = BooleanField("make forum private", default=False)
    submit = SubmitField('Post')

    #todo: set up this validator?
    def validate_name(self,name):
        forum = Forum.query.filter_by(name=name.data).first()
        if forum:
            raise ValidationError("That forum name is taken, please choose another name.")

