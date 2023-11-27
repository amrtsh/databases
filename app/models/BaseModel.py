from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    db = db

    def to_dto(self):
        raise NotImplementedError("to_dto method must be implemented in the child class")

    @classmethod
    def from_dto(cls, dto):
        raise NotImplementedError("from_dto method must be implemented in the child class")

    def to_model(self):
        return self

    @classmethod
    def from_model(cls, model):
        return model
