from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200)])
    # todo: could do the option I did on tweest
    content1 = TextAreaField("Paste or enter Content here", validators=[Length(min=20, max=10000)])
    content2 = FileField("or choose a file", validators=[])
    pic1 = FileField("Picture 1--   all forums must have at least one photo", validators=[DataRequired(),
                                                                                          FileAllowed(['jpg', 'png'])])
    pic2 = FileField("Picture 2", validators=[FileAllowed(['jpg', 'png'])])
    pic3 = FileField("Picture 3", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')


class UpdateArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    content = StringField('Email', validators=[DataRequired(), Length(min=20, max=2000)])
    picture = FileField('Update Article Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
