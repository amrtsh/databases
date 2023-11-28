from app.dao.generic_dao import GenericDAO
from app.models.person import Person


class PersonDAO(GenericDAO):
    _model = Person
