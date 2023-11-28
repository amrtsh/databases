from app.models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, Table, ForeignKeyConstraint

airport_waypoint = Table(
    'airport_waypoint',
    BaseModel.metadata,
    Column('airport_id', Integer, ForeignKey('airport.id')),
    Column('waypoint_id', Integer, ForeignKey('waypoint.id'), primary_key=True),
    ForeignKeyConstraint(['airport_id'], ['airport.id']),
    ForeignKeyConstraint(['waypoint_id'], ['waypoint.id'])
)
