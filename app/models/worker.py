from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKeyConstraint

from app import db
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey

from app.models.result import Result


class Worker(db.Model):
    """Represent a person. Attached to a Service.."""
    __tablename__ = 'pzr_worker'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))  # , db.ForeignKey('fof_tete.code_of'))
    service_id = db.Column(db.Integer, db.ForeignKey('pzr_service.id'))
    level = db.Column(db.Integer, default=1)
    ###############################
    #      result relationship    #
    results = db.relationship('Result', backref='respondent', lazy="dynamic")
    ###############################