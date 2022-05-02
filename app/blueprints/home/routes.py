from . import home as h
from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from . import home
from .forms import VacationForm
from .models import Vacation
from validators import url

@h.route('/')
def index():
    title = 'Home'

    return render_template('index.html', title = title)

@h.route('/vacation-planner')
@login_required
def vacationplanner():
    title = 'Vacation Planner'
    vacations = Vacation.query.all()
    return render_template('vacation_planner.html', title = title, vacations=vacations)
    
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
        new_plan = Vacation(plan_name=plan_name,location=location,guests=guests,date_leaving=date_leaving,date_returning=date_returning,budget=budget, user_id = current_user.id)
        flash(f"{plan_name} has been created!", "success")
        return redirect(url_for('index'))
    return render_template('create_vacation_planner.html', title = title, form = form)

@h.route('/edit-vacation/<vacation_id>', methods=["GET", "POST"])
@login_required 
def edit_vacation(vacation_id):
    vacation = Vacation.query.get_or_404(vacation_id)
    #Check if the user trying to edit the post is the current user
    if vacation.user_id != current_user.id:
        flash("You do not have edit access for this contact.", "danger")
        return redirect(url_for('index'))
    title = f"Edit Vacation: {{ Vacation.plan_name }}"
    form = VacationForm()
    if form.validate_on_submit():
        vacation.update(**form.data)
        flash(f"{vacation.plan_name} has been updated.", "success")
        return redirect(url_for('home.index'))
    return render_template('vacation_edit.html', title=title, vacation=vacation, form=form)

@h.route('/delete_vacation/<vacation_id>')
@login_required
def delete_contact(vacation_id):
    vacation = Vacation.query.get_or_404(vacation_id)
    if vacation.user_id != current_user.id:
        flash("You do not have delete access to this post.", 'secondary')
    else:
        vacation.delete()
        flash(f"{vacation} has been removed.", 'secondary')
    return redirect(url_for('home.index'))