from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Crew(db.Model):
    __tablename__ = 'crew'

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), primary_key=True, nullable=False)
    person = relationship('Person', back_populates='flight')
    flight = relationship('Flight', back_populates='person')
