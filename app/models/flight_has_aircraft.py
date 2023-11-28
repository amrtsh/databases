from app.models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, Table, ForeignKeyConstraint

flight_has_aircraft = Table('flight_has_aircraft', BaseModel.metadata,
                            Column('flight_id', Integer, ForeignKey('flight.id')),
                            Column('aircraft_id', Integer, ForeignKey('aircraft.id')),
                            ForeignKeyConstraint(['flight_id'], ['flight.id']),
                            ForeignKeyConstraint(['aircraft_id'], ['aircraft.id'])
                            )
