from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.dto.country_dto import CountryDTO
from app.models.base_model import BaseModel


class Country(BaseModel):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)

    airports = relationship('app.models.airport.Airport', backref='country', cascade='all, delete-orphan',
                            single_parent=True)

    def to_dto(self):
        return CountryDTO(name=self.name)

    @classmethod
    def from_dto(cls, data):
        if isinstance(data, CountryDTO):
            return cls(name=data.name)
        elif isinstance(data, dict):
            return cls(name=data.get('name'))
        else:
            raise ValueError("Invalid data type provided to from_dto")
