class RegistrationInfoDTO:
    def __init__(self, serial_number, manufacturing_date, registration_number, capacity_passengers, max_speed,
                 fuel_capacity, last_maintenance_date):
        self.serial_number = serial_number
        self.manufacturing_date = manufacturing_date
        self.registration_number = registration_number
        self.capacity_passengers = capacity_passengers
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.last_maintenance_date = last_maintenance_date

    def to_dict(self):
        return {
            'serial_number': self.serial_number,
            'manufacturing_date': self.manufacturing_date,
            'registration_number': self.registration_number,
            'capacity_passengers': self.capacity_passengers,
            'max_speed': self.max_speed,
            'fuel_capacity': self.fuel_capacity,
            'last_maintenance_date': self.last_maintenance_date
        }
