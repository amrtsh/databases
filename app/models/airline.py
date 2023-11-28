from sqlalchemy import Column, Integer, String, ForeignKey

from app.dto.airline_dto import AirlineDTO
from sqlalchemy.orm import relationship

from app.models.airport import Airport
from app.models.base_model import BaseModel


class Airline(BaseModel):
    __tablename__ = 'airline'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)
    website = Column(String(54), nullable=True)
    airline_code = Column(String(3), nullable=True)
    headquarters_location = Column(String(54), nullable=True)
    airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    airport = relationship('app.models.airport.Airport', backref='airline',
                           cascade='all, delete-orphan',
                           single_parent=True)
    aircraft = relationship('app.models.aircraft.Aircraft', backref='airline', cascade='all, delete-orphan',
                            single_parent=True)

    def to_dto(self):
        return AirlineDTO(
            name=self.name,
            website=self.website,
            airline_code=self.airline_code,
            headquarters_location=self.headquarters_location,
            airport=self.airport.to_dto()
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            name=data.get("name"),
            website=data.get("website"),
            airline_code=data.get("airline_code"),
            headquarters_location=data.get("headquarters_location"),
            airport=Airport.from_dto(data.get("airport"))
        )
