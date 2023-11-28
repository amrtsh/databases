from sqlalchemy import Column, Integer, DateTime, Enum
from enum import Enum as PythonEnum

from sqlalchemy.orm import declarative_base, relationship

from app.dto.flight_dto import FlightDTO

from app.models.base_model import BaseModel
from app.models import flight_has_aircraft
from app.models import crew

Base = declarative_base()


class FlightStatusEnum(PythonEnum):
    happened = 'happened'
    will_happen = 'will_happen'
    is_happening = 'is_happening'


class Flight(BaseModel):
    __tablename__ = 'flight'

    id = Column(Integer, primary_key=True, nullable=False)
    departure_datetime = Column(DateTime, nullable=True)
    arrival_datetime = Column(DateTime, nullable=True)
    status = Column(Enum(FlightStatusEnum), nullable=True)
    flight_routes = relationship('app.models.flight_route.FlightRoute', backref='flight', cascade='all, delete-orphan',
                                 single_parent=True)

    aircraft = relationship('app.models.aircraft.Aircraft', secondary='flight_has_aircraft', back_populates='flight',
                            cascade='all, delete-orphan', single_parent=True,
                            primaryjoin="and_(Flight.id == flight_has_aircraft.c.flight_id,"
                                        "Aircraft.id == flight_has_aircraft.c.aircraft_id)"
                            )

    people = relationship('app.models.person.Person', secondary='crew', backref='flight',
                          cascade='all, delete-orphan', single_parent=True,
                          primaryjoin="and_(Flight.id == crew.c.flight_id,"
                                      "Flight.id == flight_has_aircraft.c.flight_id)",
                          secondaryjoin="Person.id == crew.c.person_id"
                          )

    def to_dto(self):
        return FlightDTO(
            departure_datetime=self.departure_datetime,
            arrival_datetime=self.arrival_datetime,
            status=self.status
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            departure_datetime=data.get("departure_datetime"),
            arrival_datetime=data.get("arrival_datetime"),
            status=data.get("status")
        )
