from app.dao.generic_dao import GenericDAO
from app.models.role import Role


class RoleDAO(GenericDAO):
    _model = Role
