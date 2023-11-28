class RoleDTO:
    def __init__(self, name, role_description):
        self.name = name
        self.role_description = role_description

    def to_dict(self):
        return {
            'name': self.name,
            'role_description': self.role_description
        }
