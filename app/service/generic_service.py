class GenericService:
    _dao = None

    @classmethod
    def create(cls, dto):
        cls._dao.create(dto)

    @classmethod
    def get_by_id(cls, obj_id):
        return cls._dao.get_by_id(obj_id).to_dto()


    @classmethod
    def get_all(cls):
        objs = cls._dao.get_all()
        return [obj.to_dto() for obj in objs]

    @classmethod
    def update(cls, obj_id, dto):
        obj = cls._dao.get_by_id(obj_id)

        if obj:
            # Update only the fields present in the DTO
            for key, value in dto.items():
                setattr(obj, key, value)

            cls._dao.update(obj)
            return obj
        else:
            return None

    @classmethod
    def delete(cls, obj_id):
        cls._dao.delete(obj_id)
