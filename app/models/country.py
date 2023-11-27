from sqlalchemy import Column, Integer, String
from app.models.BaseModel import BaseModel
from app.dto.country_dto import CountryDTO

class Country(BaseModel):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(54), nullable=True)

    def to_dto(self) -> CountryDTO:
        return CountryDTO(
            name=self.name
        )

    @classmethod
    def from_dto(cls, country_dto: CountryDTO) -> 'Country':
        return cls(
            name=country_dto.name
        )
