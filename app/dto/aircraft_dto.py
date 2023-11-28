class AircraftDTO:
    def __init__(self, name, total_flight, type, airline, registration_info):
        self.name = name
        self.total_flight = total_flight
        self.type = type
        self.airline = airline
        self.registration_info = registration_info

    def to_dict(self):
        return {
            'name': self.name,
            'total_flight': self.total_flight,
            'type': self.type.to_dict() if self.type else None,
            'airline': self.airline.to_dict() if self.airline else None,
            'registration_info': self.registration_info.to_dict() if self.registration_info else None
        }
