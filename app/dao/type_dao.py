from app.dao.generic_dao import GenericDAO
from app.models.type import Type


class TypeDAO(GenericDAO):
    _model = Type
