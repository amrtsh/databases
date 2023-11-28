from app.dao.waypoint_dao import WaypointDAO
from app.service.generic_service import GenericService


class WaypointService(GenericService):
    _dao = WaypointDAO
