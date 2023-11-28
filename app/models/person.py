from sqlalchemy import Column, Integer, String, ForeignKey

from app.dto.person_dto import PersonDTO
from app.models.base_model import BaseModel
from app.models.role import Role


class Person(BaseModel):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)
    surname = Column(String(54), nullable=True)
    standing = Column(Integer, nullable=True)
    employee_id = Column(Integer, nullable=True)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)

    def to_dto(self):
        return PersonDTO(
            name=self.name,
            surname=self.surname,
            standing=self.standing,
            employee_id=self.employee_id,
            role=self.role.to_dto()
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            name=data.get("name"),
            surname=data.get("surname"),
            standing=data.get("standing"),
            employee_id=data.get("employee_id"),
            role=Role.from_dto(data.get("role"))
        )
