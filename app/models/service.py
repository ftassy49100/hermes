from sqlalchemy.sql.schema import ForeignKeyConstraint

from app import db
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class Service(db.Model):
    """Represent a person. Attached to a Service.."""
    __tablename__ = 'pzr_service'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ###############################
    #      worker relationship    #
    workers = db.relationship('Worker', backref='service', lazy="dynamic")
    ###############################
