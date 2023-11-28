from app.dao.registration_info_dao import RegistrationInfoDAO
from app.service.generic_service import GenericService


class RegistrationInfoService(GenericService):
    _dao = RegistrationInfoDAO
