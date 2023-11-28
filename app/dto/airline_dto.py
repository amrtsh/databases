class AirlineDTO:
    def __init__(self, name, website, airline_code, headquarters_location, airport):
        self.name = name
        self.website = website
        self.airline_code = airline_code
        self.headquarters_location = headquarters_location
        self.airport = airport

    def to_dict(self):
        return {
            'name': self.name,
            'website': self.website,
            'airline_code': self.airline_code,
            'headquarters_location': self.headquarters_location,
            'airport': self.airport.to_dict() if self.airport else None
        }

