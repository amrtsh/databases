from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FlightWaypoint(db.Model):
    __tablename__ = 'flight_waypoint'

    flight_route_id = db.Column(db.Integer, db.ForeignKey('flight_route.id'), primary_key=True, nullable=False)
    waypoint_id = db.Column(db.Integer, db.ForeignKey('waypoint.id'), primary_key=True, nullable=False)
    flight_route = relationship('FlightRoute', back_populates='waypoints')
    waypoint = relationship('Waypoint', back_populates='flight_route')
#     back_populates двонаправний зв'язок між двома класами
