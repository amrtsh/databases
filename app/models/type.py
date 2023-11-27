# app/models/type.py

from app.models.BaseModel import BaseModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Type(BaseModel, db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(54), nullable=True)
    latitude = db.Column(db.DECIMAL(10, 6), nullable=True)
    longitude = db.Column(db.DECIMAL(10, 6), nullable=True)

    # Add other fields and relationships as needed

    def to_dto(self):
        # Implement if needed
        pass

    @classmethod
    def from_dto(cls, type_dto):
        # Implement if needed
        pass
