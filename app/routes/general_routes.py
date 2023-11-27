from flask import jsonify, request
from app import app

class GenericRouteGenerator:
    def __init__(self, model, service, route_prefix):
        self.model = model
        self.service = service
        self.route_prefix = route_prefix

    def create_routes(self):
        route_prefix = self.route_prefix

        @app.route(f'/{route_prefix}/create', methods=['POST'])
        def create():
            data = request.get_json()
            model_instance = self.model.from_dto(data)
            self.service.create(model_instance)
            return jsonify({"message": f"{self.model.__name__} created successfully"}), 201

        @app.route(f'/{route_prefix}/<int:model_id>', methods=['GET'])
        def get_by_id(model_id):
            model_instance = self.service.get_by_id(model_id)
            if model_instance:
                return jsonify(model_instance.to_dto())
            else:
                return jsonify({"message": f"{self.model.__name__} not found"}), 404

        @app.route(f'/{route_prefix}/all', methods=['GET'])
        def get_all():
            models = self.service.get_all()
            return jsonify([model.to_dto() for model in models])

        @app.route(f'/{route_prefix}/<int:model_id>', methods=['PUT'])
        def update(model_id):
            data = request.get_json()
            model_instance = self.service.update(model_id, data)
            return jsonify({"message": f"{self.model.__name__} updated successfully"})

        @app.route(f'/{route_prefix}/<int:model_id>', methods=['DELETE'])
        def delete(model_id):
            self.service.delete(model_id)
            return jsonify({"message": f"{self.model.__name__} deleted successfully"})
