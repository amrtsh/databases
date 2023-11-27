from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Airline(db.Model):
    __tablename__ = 'airline'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(54), nullable=True)
    website = db.Column(db.String(54), nullable=True)
    airline_code = db.Column(db.String(3), nullable=True)
    headquarters_location = db.Column(db.String(54), nullable=True)
    airport_id = db.Column(db.Integer, db.ForeignKey('airport.id'), nullable=False)
    airport = relationship('Airport')
