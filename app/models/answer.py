from sqlalchemy.sql.schema import ForeignKeyConstraint

from app import db
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey, Boolean


class Answer(db.Model):
    """Represent an answer. attached to a question ; one is correct, the other are not."""
    __tablename__ = 'pzr_answer'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(300))
    question_id = db.Column(db.Integer, db.ForeignKey('pzr_question.id'))
    right_answer = db.Column(db.Boolean, default=False, nullable=False)
    explanation = db.Column(db.String)
    ###############################
    #      result relationship    #
    results = db.relationship('Result', backref='worker', lazy="dynamic")
    ###############################
