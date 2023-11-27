from app import app
from app.config import Config
from app.models.BaseModel import db
# from app.models.aircraft import Aircraft
from app.models.airline import Airline
from app.models.country import Country
from app.routes.general_routes import GenericRouteGenerator
# from app.service.aircraft_service import AircraftService
from app.service.country_service import CountryService

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1111@localhost/mydb'
# db.init_app(app)

# AircraftRouteGenerator = GenericRouteGenerator(Aircraft, AircraftService, 'aircraft')
# AircraftRouteGenerator.create_routes()

CountryRouteGenerator = GenericRouteGenerator(Country, CountryService, 'country')
CountryRouteGenerator.create_routes()

# AirlineRouteGenerator = GenericRouteGenerator(Airline, AirlineService, 'airline')
# AirlineRouteGenerator.create_routes()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)