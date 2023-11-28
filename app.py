from app import app
from app.models.aircraft import Aircraft
from app.models.airline import Airline
from app.models.airport import Airport
from app.models.country import Country
from app.models.flight import Flight
from app.models.flight_route import FlightRoute
from app.models.person import Person
from app.models.registration_info import RegistrationInfo
from app.models.role import Role
from app.models.type import Type
from app.models.waypoint import Waypoint
from app.routes.generic_route import GenericRouteGenerator
from app.service.aircraft_service import AircraftService
from app.service.airline_service import AirlineService
from app.service.airport_service import AirportService
from app.service.country_service import CountryService
from app.service.flight_route_service import FlightRouteService
from app.service.flight_service import FlightService
from app.service.person_service import PersonService
from app.service.registration_info_service import RegistrationInfoService
from app.service.role_service import RoleService
from app.service.type_service import TypeService
from app.service.waypoint_service import WaypointService

CountryRouteGenerator = GenericRouteGenerator(Country, CountryService, 'country')
CountryRouteGenerator.create_routes()

AircraftRouteGenerator = GenericRouteGenerator(Aircraft, AircraftService, 'aircraft')
AircraftRouteGenerator.create_routes()

AirlineRouteGenerator = GenericRouteGenerator(Airline, AirlineService, 'airline')
AirlineRouteGenerator.create_routes()

AirportRouteGenerator = GenericRouteGenerator(Airport, AirportService, 'airport')
AirportRouteGenerator.create_routes()

FlightRouteGenerator = GenericRouteGenerator(Flight, FlightService, 'flight')
FlightRouteGenerator.create_routes()

FlightRouteRouteGenerator = GenericRouteGenerator(FlightRoute, FlightRouteService, 'flight_route')
FlightRouteRouteGenerator.create_routes()

PersonRouteGenerator = GenericRouteGenerator(Person, PersonService, 'person')
PersonRouteGenerator.create_routes()

RegistrationInfoRouteGenerator = GenericRouteGenerator(RegistrationInfo, RegistrationInfoService, 'registration_info')
RegistrationInfoRouteGenerator.create_routes()

RoleRouteGenerator = GenericRouteGenerator(Role, RoleService, 'role')
RoleRouteGenerator.create_routes()

TypeRouteGenerator = GenericRouteGenerator(Type, TypeService, 'type')
TypeRouteGenerator.create_routes()

WaypointRouteGenerator = GenericRouteGenerator(Waypoint, WaypointService, 'waypoint')
WaypointRouteGenerator.create_routes()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
