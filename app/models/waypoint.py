from sqlalchemy import Column, Integer, String, DECIMAL

from app.dto.waypoint_dto import WaypointDTO
from app.models import airport_waypoint
from app.models import flight_waypoint
from app.models.base_model import BaseModel


class Waypoint(BaseModel):
    __tablename__ = 'waypoint'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)
    latitude = Column(DECIMAL(10, 6), nullable=True)
    longitude = Column(DECIMAL(10, 6), nullable=True)

    def to_dto(self):
        return WaypointDTO(
            name=self.name,
            latitude=self.latitude,
            longitude=self.longitude
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            name=data.get("name"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude")
        )
