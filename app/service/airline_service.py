from app.dao.airline_dao import AirlineDAO
from app.service.generic_service import GenericService


class AirlineService(GenericService):
    _dao = AirlineDAO
