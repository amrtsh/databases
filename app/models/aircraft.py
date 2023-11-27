# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from flask_sqlalchemy import SQLAlchemy
# from .type import Type
#
# from app.dto.aircraft_dto import AircraftDTO
# from app.models.BaseModel import BaseModel
#
# db = SQLAlchemy()
#
#
# class Aircraft(BaseModel, db.Model):
#     __tablename__ = 'aircraft'
#
#     id = Column(Integer, primary_key=True, nullable=False)
#     name = Column(String(54), nullable=True)
#     total_flight = Column(Integer, nullable=True)
#     type_id = Column(Integer, ForeignKey('type.id'), nullable=False)
#     type = relationship('Type')
#     airline_id = Column(Integer, ForeignKey('airline.id'), nullable=False)
#     airline = relationship('Airline')
#     registration_info_id = Column(Integer, ForeignKey('registration_info.id'), nullable=False)
#     registration_info = relationship('RegistrationInfo')
#
#     def to_dto(self) -> AircraftDTO:
#         return AircraftDTO(
#             name=self.name,
#             total_flight=self.total_flight,
#             type_id=self.type_id,
#             airline_id=self.airline_id,
#             registration_info_id=self.registration_info_id
#         )
#
#     @classmethod
#     def from_dto(cls, aircraft_dto: AircraftDTO) -> 'Aircraft':
#         return cls(
#             name=aircraft_dto.name,
#             total_flight=aircraft_dto.total_flight,
#             type_id=aircraft_dto.type_id,
#             airline_id=aircraft_dto.airline_id,
#             registration_info_id=aircraft_dto.registration_info_id
#         )
