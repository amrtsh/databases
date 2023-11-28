class FlightRouteDTO:
    def __init__(self, distance_km, route_description, flight):
        self.distance_km = distance_km
        self.route_description = route_description
        self.flight = flight

    def to_dict(self):
        return {
            'distance_km': self.distance_km,
            'route_description': self.route_description,
            'flight': self.flight.to_dict() if self.flight else None
        }
