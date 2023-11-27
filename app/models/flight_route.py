from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FlightRoute(db.Model):
    __tablename__ = 'flight_route'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    distance_km = db.Column(db.Integer, nullable=True)
    route_description = db.Column(db.String(100), nullable=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
    flight = relationship('Flight')
