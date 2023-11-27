class GenericService:
    _dao = None

    @classmethod
    def create(cls, dto):
        obj = cls._dao.get_model().from_dto(dto)
        cls._dao.create(obj)

    @classmethod
    def get_by_id(cls, obj_id):
        return cls._dao.get_by_id(obj_id)

    @classmethod
    def get_all(cls):
        objs = cls._dao.get_all()
        return [obj.to_dto() for obj in objs]

    @classmethod
    def update(cls, obj_id, dto):
        obj = cls._dao.get_by_id(obj_id)

        if obj:
            for key, value in dto.__dict__.items():
                setattr(obj, key, value)

            cls._dao.update(obj)

        return obj

    @classmethod
    def delete(cls, obj_id):
        cls._dao.delete(obj_id)
