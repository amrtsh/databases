from app.dao.generic_dao import GenericDAO
from app.models.airport import Airport


class AirportDAO(GenericDAO):
    _model = Airport
