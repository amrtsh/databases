class FlightDTO:
    def __init__(self, departure_datetime, arrival_datetime, status):
        self.departure_datetime = departure_datetime
        self.arrival_datetime = arrival_datetime
        self.status = status

    def to_dict(self):
        from app.models.flight import FlightStatusEnum
        return {
            'departure_datetime': self.departure_datetime,
            'arrival_datetime': self.arrival_datetime,
            'status': self.status.value if isinstance(self.status, FlightStatusEnum) else self.status
        }
