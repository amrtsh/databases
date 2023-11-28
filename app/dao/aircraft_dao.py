from app.dao.generic_dao import GenericDAO
from app.models.aircraft import Aircraft


class AircraftDAO(GenericDAO):
    _model = Aircraft
