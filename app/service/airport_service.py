from app.dao.airport_dao import AirportDAO
from app.service.generic_service import GenericService


class AirportService(GenericService):
    _dao = AirportDAO
