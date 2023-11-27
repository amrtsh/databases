from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FlightHasAircraft(db.Model):
    __tablename__ = 'flight_has_aircraft'

    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), primary_key=True, nullable=False)
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.id'), primary_key=True, nullable=False)
    aircraft = relationship('Aircraft', back_populates='flight')
    flight = relationship('Flight', back_populates='person')
