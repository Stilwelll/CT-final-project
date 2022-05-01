from app import db, login
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo 


class VacationForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired(), Email()])
    plan_name = StringField('Vacation Plan Name', validators=[DataRequired()])
    guests = IntegerField('Additonal Guests', validators=[DataRequired()])
    date_leaving = DateField('Date Leaving', validators=[DataRequired()], format="%m-%d-%Y")
    date_returning = DateField('Date Returning', validators=[DataRequired()], format="%m-%d-%Y")
    budget = FloatField('Budget', validators=[DataRequired()])
    submit = SubmitField('Submit')
