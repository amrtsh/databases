from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.dto.aircraft_dto import AircraftDTO
from app.models.base_model import BaseModel


class Aircraft(BaseModel):
    __tablename__ = 'aircraft'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)
    total_flight = Column(Integer, nullable=True)
    type_id = Column(Integer, ForeignKey('type.id'), nullable=False)
    airline_id = Column(Integer, ForeignKey('airline.id'), nullable=False)
    registration_info_id = Column(Integer, ForeignKey('registration_info.id'), nullable=False)
    flight = relationship('app.models.flight.Flight', secondary='flight_has_aircraft', back_populates='aircraft',
                          cascade='all, delete-orphan', single_parent=True,
                          primaryjoin="Aircraft.id == flight_has_aircraft.c.aircraft_id",
                          secondaryjoin="Flight.id == flight_has_aircraft.c.flight_id"
                          )

    def to_dto(self):
        return AircraftDTO(
            name=self.name,
            total_flight=self.total_flight,
            type=self.type.to_dto() if self.type else None,
            airline=self.airline.to_dto() if self.airline else None,
            registration_info=self.registration_info.to_dto() if self.registration_info else None
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            name=data.get("name"),
            total_flight=data.get("total_flight"),
            type_id=int(data.get("type_id")) if data.get("type_id") else None,
            airline_id=int(data.get("airline_id")) if data.get("airline_id") else None,
            registration_info_id=int(data.get("registration_info_id")) if data.get("registration_info_id") else None
        )
