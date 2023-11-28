from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.dto.registration_info_dto import RegistrationInfoDTO
from app.models.base_model import BaseModel


class RegistrationInfo(BaseModel):
    __tablename__ = 'registration_info'

    id = Column(Integer, primary_key=True, nullable=False)
    serial_number = Column(Integer, nullable=True)
    manufacturing_date = Column(DateTime, nullable=True)
    registration_number = Column(String(10), nullable=True)
    capacity_passengers = Column(Integer, nullable=True)
    max_speed = Column(Integer, nullable=True)
    fuel_capacity = Column(Integer, nullable=True)
    last_maintenance_date = Column(DateTime, nullable=True)
    aircraft = relationship('app.models.aircraft.Aircraft', backref='registration_info', cascade='all, delete-orphan',
                            single_parent=True)

    def to_dto(self):
        return RegistrationInfoDTO(
            serial_number=self.serial_number,
            manufacturing_date=self.manufacturing_date,
            registration_number=self.registration_number,
            capacity_passengers=self.capacity_passengers,
            max_speed=self.max_speed,
            fuel_capacity=self.fuel_capacity,
            last_maintenance_date=self.last_maintenance_date
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            serial_number=data.get("serial_number"),
            manufacturing_date=data.get("manufacturing_date"),
            registration_number=data.get("registration_number"),
            capacity_passengers=data.get("capacity_passengers"),
            max_speed=data.get("max_speed"),
            fuel_capacity=data.get("fuel_capacity"),
            last_maintenance_date=data.get("last_maintenance_date")
        )
