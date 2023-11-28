from app import db


class BaseModel(db.Model):
    __abstract__ = True

    def to_dto(self):
        raise NotImplementedError("to_dto method must be implemented in the child class")

    def from_dto(self, dto):
        raise NotImplementedError("from_dto method must be implemented in the child class")
