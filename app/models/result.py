from sqlalchemy.sql.schema import ForeignKeyConstraint

from app import db
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime


class Result(db.Model):
    """Represent an answer made by a worker."""
    __tablename__ = 'pzr_result'
    result_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('pzr_question.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('pzr_answer.id'))
    worker_id = db.Column(db.Integer, db.ForeignKey('pzr_worker.id'))
    storage_date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, question_id, answer_id, worker_id):
        self.question_id = question_id
        self.answer_id = answer_id
        self.worker_id = worker_id
        self.storage_dage = datetime.now()
