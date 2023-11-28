from app.dao.generic_dao import GenericDAO
from app.models.flight_route import FlightRoute


class FlightRouteDAO(GenericDAO):
    _model = FlightRoute
