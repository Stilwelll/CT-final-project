from . import home as h
from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from . import home
from .forms import VacationForm
from .models import Vacation

@h.route('/')
def index():
    title = 'Home'

    return render_template('index.html', title = title)

@h.route('/vacation-planner')
@login_required
def vacationplanner():
    title = 'Vacation Planner'

    return render_template('vacation_planner.html', title = title)
    
@h.route('/create-vacation-planner', methods = ['GET', 'POST'])
@login_required
def createvacationplanner():
    title = 'Create Vacation Planner'
    form = VacationForm()

    if form.validate_on_submit():
        plan_name = form.plan_name.data
        location = form.location.data
        guests = form.guests.data
        date_leaving = form.date_leaving.data
        date_returning = form.date_returning.data
        budget = form.budget.data

        flash(f"{plan_name} has been created!", "success")
        new_plan = Vacation(title=title,location=location,guests=guests,date_leaving=date_leaving,date_returning=date_returning,budget=budget)
        return redirect(url_for('home.vacation_planner'))
    return render_template('create_vacation_planner.html', title = title, form = form)