from app.dao.generic_dao import GenericDAO
from app.models.waypoint import Waypoint


class WaypointDAO(GenericDAO):
    _model = Waypoint
