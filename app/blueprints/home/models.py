from webbrowser import get
from app import db, login
from app.blueprints.auth.models import User
from flask_login import current_user


class Vacation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    date_leaving = db.Column(db.Date, nullable=False)
    date_returning = db.Column(db.Date, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Plan Name | {self.plan_name}>"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in {'plan_name','location','guests','date_leaving','date_returning','budget'}:
                setattr(self, key, value)
            db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()