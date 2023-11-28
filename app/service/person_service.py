from app.dao.person_dao import PersonDAO
from app.service.generic_service import GenericService


class PersonService(GenericService):
    _dao = PersonDAO
