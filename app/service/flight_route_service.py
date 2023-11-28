from app.dao.flight_route_dao import FlightRouteDAO
from app.service.generic_service import GenericService


class FlightRouteService(GenericService):
    _dao = FlightRouteDAO
