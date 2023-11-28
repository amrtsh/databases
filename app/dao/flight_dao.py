from app.dao.generic_dao import GenericDAO
from app.models.flight import Flight


class FlightDAO(GenericDAO):
    _model = Flight
