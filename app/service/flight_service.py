from app.dao.flight_dao import FlightDAO
from app.service.generic_service import GenericService


class FlightService(GenericService):
    _dao = FlightDAO
