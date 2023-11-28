class AirportDTO:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def to_dict(self):
        return {
            'name': self.name,
            'country': self.country.to_dict() if self.country else None
        }