from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, FileField, IntegerField,BooleanField, TextAreaField,PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from tweestmaster.models import Forum


class ForumForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField("Describe your forum", validators=[DataRequired()])
    picture = FileField("Select your Forum photo", validators=[FileAllowed(['jpg', 'png'])])
    is_public = BooleanField("Make Forum private", default=False)
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=64)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Post')

    def validate_name(self,name):
        forum = Forum.query.filter_by(name=name.data).first()
        if forum:
            raise ValidationError("That forum name is taken, please choose another name.")

