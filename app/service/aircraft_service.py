from app.dao.aircraft_dao import AircraftDAO
from app.service.generic_service import GenericService


class AircraftService(GenericService):
    _dao = AircraftDAO
