from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo, ValidationError
from application.models import User
from flask_login import current_user

class DietForm(FlaskForm):
    diet_name = StringField('Diet name', validators=[DataRequired(),Length(min=1, max=128)])
    description = StringField('Description', validators=[DataRequired(), Length(min=1, max=512)])
    submit = SubmitField('Create Diet')



class FoodForm(FlaskForm):
    food_name = StringField('Food', validators=[DataRequired(), Length(min=1, max=128)])
    calories = IntegerField('Calories kcal', validators=[NumberRange(min=0, max=100000)])
    submit = SubmitField('Create Food')



class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')



class RegistrationForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(),Length(min=1, max=64)])
	surname = StringField('Surname', validators=[DataRequired(),Length(min=1, max=64)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError('Email is already in use!')



class UpdateAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=1, max=64)])
    surname = StringField('Surname', validators=[DataRequired(),Length(min=1, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is already in use!')


