from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.orm import model_form
from app.models.question import Question


class PointingForm(Form):
    worker_id = IntegerField('worker_id', [DataRequired()])