from app.models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, Table, ForeignKeyConstraint

flight_waypoint = Table('flight_waypoint', BaseModel.metadata,
                        Column('waypoint_id', Integer, ForeignKey('waypoint.id')),
                        Column('flight_route_id', Integer, ForeignKey('flight_route.id')),
                        ForeignKeyConstraint(['waypoint_id'], ['waypoint.id']),
                        ForeignKeyConstraint(['flight_route_id'], ['flight_route.id'])
                        )
