from app import db, login
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired


class VacationForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    plan_name = StringField('Vacation Plan Name')
    guests = IntegerField('Additonal Guests')
    date_leaving = DateField('Date Leaving')
    date_returning = DateField('Date Returning')
    budget = FloatField('Budget')
    submit = SubmitField('Submit')


    
    
    
    
