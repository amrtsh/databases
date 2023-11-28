from app.dao.role_dao import RoleDAO
from app.service.generic_service import GenericService


class RoleService(GenericService):
    _dao = RoleDAO
