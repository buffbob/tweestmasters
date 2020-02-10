from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.fields.html5 import IntegerRangeField, DecimalRangeField




class ReviewForm(FlaskForm):
    entertainment_score = IntegerRangeField('Entertainment Value', default=0)
    style_score = IntegerRangeField("Style Value", default=0)
    content = TextAreaField("Place your textual review here")
