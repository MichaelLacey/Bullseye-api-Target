from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class review_form(FlaskForm):
    product_id = IntegerField('Product Id', validators=[DataRequired()])
    user_id = IntegerField('User Id:', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit') 