from app.dao.generic_dao import GenericDAO
from app.models.airline import Airline


class AirlineDAO(GenericDAO):
    _model = Airline
