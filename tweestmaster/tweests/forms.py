from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileAllowed
from flask_login import current_user
from tweestmaster.models import User

class TweestForm(FlaskForm):
    title = StringField('Your tweesst title', validators=[DataRequired(), Length(min=2, max=100)])
    content1 = TextAreaField("Paste your tweesst content here")
    # need validation that tweest if not none is of right length
    content2 = FileField('or choose file')
    # need validation that content1 and content2 are both not none.
    # todo: fixing a routing and issue problem
    # will need validation to confirm that one of the contents is occupied **************
    submit = SubmitField('Post')

class UpdateTweestForm(FlaskForm):

    title = StringField('Title',
                           validators=[DataRequired(), Length(min=2, max=20)])
    content1 = StringField('Edit your content here',
                        validators=[DataRequired(), Email()])
    content2 = FileField('or submit a new file', validators=[Length(min=20, max=5000)])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            raise ValidationError('That username is taken. Please choose a different one.')

