from sqlalchemy.sql.schema import ForeignKeyConstraint

from app import db
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class Question(db.Model):
    """Represent a person. Attached to a Service.."""
    __tablename__ = 'pzr_question'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(300))
    category_id = db.Column(db.Integer, db.ForeignKey('pzr_category.id'))
    level = db.Column(db.Integer, default=1)
    ###############################
    #     answers relationship    #
    answers = db.relationship('Answer', backref='question', lazy="dynamic")
    ###############################
    ###############################
    #     results relationship    #
    results = db.relationship('Result', backref='question', lazy="dynamic")
    ###############################