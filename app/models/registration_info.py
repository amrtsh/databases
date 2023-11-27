from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RegistrationInfo(db.Model):
    __tablename__ = 'registration_info'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    serial_number = db.Column(db.Integer, nullable=True)
    manufacturing_date = db.Column(db.DateTime, nullable=True)
    registration_number = db.Column(db.String(10), nullable=True)
    capacity_passengers = db.Column(db.Integer, nullable=True)
    max_speed = db.Column(db.Integer, nullable=True)
    fuel_capacity = db.Column(db.Integer, nullable=True)
    last_maintenance_date = db.Column(db.DateTime, nullable=True)
