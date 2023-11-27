# from app.dao.aircraft_dao import AircraftDAO
from app.dao.coutry_dao import CountryDAO
from app.service.general_service import GenericService


class CountryService(GenericService):
    _dao = CountryDAO
