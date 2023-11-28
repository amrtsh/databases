from app.dao.country_dao import CountryDAO
from app.service.generic_service import GenericService


class CountryService(GenericService):
    _dao = CountryDAO
