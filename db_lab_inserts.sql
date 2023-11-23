INSERT INTO mydb.country (id, name) VALUES
(1, 'United States'),
(2, 'Brazil'),
(3, 'Germany'),
(4, 'France'),
(5, 'Italy');

INSERT INTO mydb.airport (id, name, country_id) VALUES
(1, 'Boryspil', 1),
(2, 'Hartsfield-Jackson Atlanta', 1),
(3, 'Brasília', 2),
(4, 'Frankfurt Airport', 3),
(5, 'Paris Orly Airport', 4),
(6, 'Milan Malpensa Airport', 5),
(7, 'Warsaw Chopin Airport', 3),
(8, 'Bandaranaike', 2);

INSERT INTO mydb.airline (id, name, website, airline_code, 
headquarters_location, airport_id) VALUES
(1, 'Airline 1', 'www.airline1.com', 'AA1', 'Location 1', 1),
(2, 'Airline 2', 'www.airline2.com', 'AA2', 'Location 2', 2),
(3, 'Airline 3', 'www.airline3.com', 'AA3', 'Location 3', 3),
(4, 'Airline 4', 'www.airline4.com', 'AA4', 'Location 4', 4),
(5, 'Airline 5', 'www.airline5.com', 'AA5', 'Location 5', 5),
(6, 'Airline 6', 'www.airline6.com', 'AA6', 'Location 6', 6),
(7,'Airline 7', 'www.airline7.com', 'AA7', 'Location 7', 7),
(8, 'Airline 8', 'www.airline8.com', 'AA8', 'Location 8', 8);

INSERT INTO mydb.type (id, name) VALUES
(1, 'Commercial Airliners'),
(2, 'General Aviation'),
(3, 'Military Aircraft'),
(4, 'Helicopters'),
(5, 'Cargo Aircraft'),
(6, 'Business Jets'),
(7, 'Regional Airliners'),
(8, 'Gliders');

INSERT INTO mydb.registration_info (id, serial_number, manufacturing_date, 
registration_number, capacity_passengers, max_speed, fuel_capacity, 
last_maintenance_date) VALUES
(1, 12345, '2020-09-26', 'ABC123', 150, 600, 10000, '2023-08-15'),
(2, 54321, '2020-09-15', 'XYZ789', 180, 650, 12000, '2023-08-10'),
(3, 98765, '2017-08-30', 'DEF456', 130, 550, 8000, '2023-09-02'),
(4, 45678, '2020-09-10', 'GHI789', 160, 620, 11000, '2023-08-20'),
(5, 23456, '2017-09-05', 'JKL123', 140, 580, 9500, '2023-09-05'),
(6, 87654, '2017-09-18', 'MNO456', 170, 630, 10500, '2023-08-25'),
(7, 34567, '2020-09-02', 'PQR789', 190, 670, 12500, '2023-09-10'),
(8, 65432, '2017-09-12', 'STU123', 120, 520, 7500, '2023-09-15');

INSERT INTO mydb.aircraft (id, name, total_flight, registration_info_id, 
type_id, airline_id)
VALUES
(1, 'SkyRider', 100, 1, 1, 1),
(2, 'AeroJet Starlight', 120, 2, 2, 2),
(3, 'Horizon', 130, 3, 3, 3),
(4, 'Thunderbird', 110, 4, 4, 4),
(5, 'TurboWing', 150, 5, 5, 5),
(6, 'Phoenix Voyager', 140, 6, 6, 6),
(7, 'Falcon', 160, 7, 7, 7),
(8, 'Falcon Skyhawk', 170, 8, 8, 8);

INSERT INTO mydb.role (id, name, role_description) VALUES
(1, 'Pilot', 'Responsible for flying and navigating the aircraft.'),
(2, 'Flight Attendant', 'Ensures passenger safety, comfort, and service 
during the flight.'),
(3, 'Co-Pilot', 'Assists the pilot in flying and navigating the 
aircraft.');

INSERT INTO mydb.person (id, name, surname, standing, employee_id, 
role_id) VALUES
(1, 'John', 'Smith', 1, 123, 1),
(2, 'Sarah', 'Johnson', 2, 234, 2),
(3, 'Michael', 'Brown', 3, 345, 3),
(4, 'Emily', 'Williams', 4, 456, 1),
(5, 'David', 'Anderson', 5, 567, 2),
(6, 'Jessica', 'Davis', 6, 678, 3),
(7, 'James', 'Wilson', 7, 789, 1),
(8, 'Olivia', 'Jackson', 8, 890, 2);

INSERT INTO mydb.crew (person_id, aircraft_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6);

INSERT INTO mydb.flight (id, aircraft_id, departure_datetime, 
arrival_datetime, status) VALUES
(1, 1, '2023-09-26 08:00:00', '2023-09-26 10:00:00', 'happened'),
(2, 2, '2023-09-27 09:00:00', '2023-09-27 11:00:00', 'will happen'),
(3, 3, '2023-09-28 10:00:00', '2023-09-28 12:00:00', 'is happening'),
(4, 4, '2023-09-29 11:00:00', '2023-09-29 13:00:00', 'happened'),
(5, 5, '2023-09-30 12:00:00', '2023-09-30 14:00:00', 'will happen'),
(6, 6, '2023-10-01 13:00:00', '2023-10-01 15:00:00', 'is happening'),
(7, 7, '2023-10-02 14:00:00', '2023-10-02 16:00:00', 'happened'),
(8, 8, '2023-10-03 15:00:00', '2023-10-03 17:00:00', 'will happen');

INSERT INTO mydb.flight_route (id, distance_km, route_description, 
flight_id) VALUES
(1, 500, 'Route 1 Description', 1),
(2, 600, 'Route 2 Description', 2),
(3, 700, 'Route 3 Description', 3),
(4, 800, 'Route 4 Description', 4),
(5, 900, 'Route 5 Description', 5),
(6, 1000, 'Route 6 Description', 6),
(7, 1100, 'Route 7 Description', 7),
(8, 1200, 'Route 8 Description', 8);

INSERT INTO mydb.waypoint (name, latitude, longitude) VALUES
('Waypoint 1', 50.3402, 30.8931),
('Waypoint 2', 33.6407, -84.4277),
('Waypoint 3', -15.8697 , -47.9177),
('Waypoint 4', 52.1657, 20.9671),
('Waypoint 5', 45.6270, 8.7120),
('Waypoint 6', 50.0333, 8.5706),
('Waypoint 7', 7.1808, 79.8844),
('Waypoint 8', 48.7262 , 2.3654);

INSERT INTO mydb.flight_waypoint (flight_id, waypoint_id, waypoint_order) 
VALUES
(1, 1, 1),
(1, 2, 2),
(1, 3, 3),
(2, 1, 1),
(2, 2, 2),
(3, 1, 1),
(3, 3, 2);	

INSERT INTO mydb.airport_waypoint (airport_id, waypoint_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6);

