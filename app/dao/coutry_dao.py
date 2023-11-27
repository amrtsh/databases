from app.dao.general_dao import GenericDAO
from app.models.country import Country


class CountryDAO(GenericDAO):
    _model = Country
