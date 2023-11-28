from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.dto.role_dto import RoleDTO
from app.models.base_model import BaseModel


class Role(BaseModel):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)
    role_description = Column(String(100), nullable=True)
    person = relationship('app.models.person.Person', backref='role', cascade='all, delete-orphan', single_parent=True)

    def to_dto(self):
        return RoleDTO(
            name=self.name,
            role_description=self.role_description
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            name=data.get("name"),
            role_description=data.get("role_description")
        )
