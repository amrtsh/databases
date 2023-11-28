class PersonDTO:
    def __init__(self, name, surname, standing, employee_id, role):
        self.name = name
        self.surname = surname
        self.standing = standing
        self.employee_id = employee_id
        self.role = role

    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'standing': self.standing,
            'employee_id': self.employee_id,
            'role': self.role.to_dict() if self.role else None
        }
