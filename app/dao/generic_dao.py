from app import db


class GenericDAO:
    _model = None

    def __init__(self, model):
        self._model = model

    def get_model(self):
        return self._model

    @classmethod
    def create(cls, obj):
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def get_by_id(cls, obj_id):
        return cls._model.query.get(obj_id)

    @classmethod
    def get_all(cls):
        return db.session.query(cls._model).all()

    @classmethod
    def update(cls, obj):
        db.session.commit()

    @classmethod
    def delete(cls, obj_id):
        obj = cls._model.query.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()
