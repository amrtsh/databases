from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from app.dto.flight_route_dto import FlightRouteDTO
from app.models.base_model import BaseModel
from app.models.flight import Flight

Base = declarative_base()


class FlightRoute(BaseModel):
    __tablename__ = 'flight_route'

    id = Column(Integer, primary_key=True, nullable=False)
    distance_km = Column(Integer, nullable=True)
    route_description = Column(String(100), nullable=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)

    waypoints = relationship(
        'Waypoint',
        secondary='flight_waypoint',
        backref='flight_routes',
        primaryjoin="FlightRoute.id == flight_waypoint.c.flight_route_id",
        secondaryjoin="Waypoint.id == flight_waypoint.c.waypoint_id"
    )

    def to_dto(self):
        return FlightRouteDTO(
            distance_km=self.distance_km,
            route_description=self.route_description,
            flight=self.flight.to_dto() if self.flight else None
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            distance_km=data.get("distance_km"),
            route_description=data.get("route_description"),
            flight=Flight.from_dto(data.get("flight"))
        )
