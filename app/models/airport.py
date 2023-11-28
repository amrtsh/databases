from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, declarative_base

from app.dto.airport_dto import AirportDTO
from app.models.base_model import BaseModel
from app.models.country import Country

Base = declarative_base()


class Airport(BaseModel):
    __tablename__ = 'airport'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)
    country_id = Column(Integer, ForeignKey('country.id'), nullable=False)

    waypoints = relationship(
        'Waypoint',
        secondary='airport_waypoint',
        backref='airports',
        primaryjoin="Airport.id == airport_waypoint.c.airport_id",
        secondaryjoin="Waypoint.id == airport_waypoint.c.waypoint_id"
    )

    def to_dto(self):
        return AirportDTO(
            name=self.name,
            country=self.country.to_dto()
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            name=data.get("name"),
            country=Country.from_dto(data.get("country"))
        )
