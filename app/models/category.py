from sqlalchemy.sql.schema import ForeignKeyConstraint

from app import db
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class Category(db.Model):
    """Category of questions"""
    __tablename__ = 'pzr_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ###############################
    #    questions relationship   #
    questions = db.relationship('Question', backref='category', lazy="dynamic")
    ###############################
