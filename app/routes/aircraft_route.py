# from flask import render_template, request, redirect, jsonify
# from app import app
#
# from app.models.aircraft import db, Aircraft
# from app.service.aircraft_service import AircraftService
#
#
# @app.route('/aircraft/create', methods=['POST'])
# def create_aircraft():
#     aircraft = request.get_json()
#     AircraftService.create(aircraft)
#     return jsonify({"message": "Aircraft created successfully"}), 201
#
#
# @app.route('/aircraft/<int:aircraft_id>', methods=['GET'])
# def get_aircraft_by_id(aircraft_id):
#     aircraft = AircraftService.get_by_id(aircraft_id)
#     if aircraft:
#         return jsonify(aircraft)
#     else:
#         return jsonify({"message": "Aircraft not found"}), 404
#
#
# @app.route('/aircrafts', methods=['GET'])
# def get_all_aircrafts():
#     aircrafts = AircraftService.get_all()
#     return jsonify(aircrafts)
#
#
# @app.route('/aircraft/<int:aircraft_id>', methods=['PUT'])
# def update_aircraft(aircraft_id):
#     aircraft = request.get_json()
#     AircraftService.update(aircraft_id, aircraft)
#     return jsonify({"message": "Aircraft updated successfully"})
#
#
# @app.route('/aircraft/<int:aircraft_id>', methods=['DELETE'])
# def delete_aircraft(aircraft_id):
#     AircraftService.delete(aircraft_id)
#     return jsonify({"message": "Aircraft deleted successfully"})
