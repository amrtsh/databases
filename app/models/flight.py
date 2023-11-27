from enum import Enum as PythonEnum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FlightStatusEnum(PythonEnum):
    happened = 'happened'
    will_happen = 'will happen'
    is_happening = 'is happening'


class Flight(db.Model):
    __tablename__ = 'flight'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    departure_datetime = db.Column(db.DateTime, nullable=True)
    arrival_datetime = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Enum(FlightStatusEnum), nullable=True)
