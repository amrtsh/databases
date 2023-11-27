from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Airport(db.Model):
    __tablename__ = 'airport'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(54), nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    country = relationship('Country')
