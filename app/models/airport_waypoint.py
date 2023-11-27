from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AirportWaypoint(db.Model):
    __tablename__ = 'airport_waypoint'

    airport_id = db.Column(db.Integer, db.ForeignKey('airport.id'), primary_key=True)
    waypoint_id = db.Column(db.Integer, db.ForeignKey('waypoint.id'), primary_key=True)
    airport = relationship('Airport', back_populates='waypoints')
    waypoint = relationship('Waypoint', back_populates='airports')
#     back_populates двонаправний зв'язок між двома класами
