from app.models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, Table, ForeignKeyConstraint

crew = Table('crew', BaseModel.metadata, Column('flight_id', Integer, ForeignKey('flight.id')),
             Column('person_id', Integer, ForeignKey('person.id')),
             ForeignKeyConstraint(['flight_id'], ['flight.id']),
             ForeignKeyConstraint(['person_id'], ['person.id'])
             )
