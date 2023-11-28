from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.dto.type_dto import TypeDTO
from app.models.base_model import BaseModel


class Type(BaseModel):
    __tablename__ = 'type'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)
    aircraft = relationship('app.models.aircraft.Aircraft', backref='type', cascade='all, delete-orphan',
                            single_parent=True)

    def to_dto(self):
        return TypeDTO(
            name=self.name
        )

    @classmethod
    def from_dto(cls, data):
        return cls(
            name=data.get("name")
        )
