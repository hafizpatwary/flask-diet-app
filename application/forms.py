from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class DietForm(FlaskForm):
    diet_name = StringField('Diet name', validators=[DataRequired(),Length(min=1, max=128)])
    description = StringField('Description', validators=[DataRequired(), Length(min=1, max=512)])
    submit = SubmitField('Create Diet')



class FoodForm(FlaskForm):
    food_name = StringField('Food', validators=[DataRequired(), Length(min=1, max=128)])
    calories = IntegerField('Calories kcal', validators=[NumberRange(min=0, max=100000)])
    submit = SubmitField('Create Food')

