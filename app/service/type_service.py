from app.dao.type_dao import TypeDAO
from app.service.generic_service import GenericService


class TypeService(GenericService):
    _dao = TypeDAO
