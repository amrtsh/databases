from app.dao.generic_dao import GenericDAO
from app.models.registration_info import RegistrationInfo


class RegistrationInfoDAO(GenericDAO):
    _model = RegistrationInfo
