SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS mydb DEFAULT CHARACTER SET utf8 ;
USE mydb ;

-- -----------------------------------------------------
-- Table mydb.registration_info
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.registration_info (
  id INT NOT NULL,
  serial_number INT NULL,
  manufacturing_date DATE NULL,
  registration_number VARCHAR(10) NULL,
  capacity_passengers INT NULL,
  max_speed INT NULL,
  fuel_capacity INT NULL,
  last_maintenance_date DATE NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.type
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.type (
  id INT NOT NULL,
  name VARCHAR(20) NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.country
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.country (
  id INT NOT NULL,
  name VARCHAR(20) NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.airport
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.airport (
  id INT NOT NULL,
  name VARCHAR(30) NULL,
  country_id INT NOT NULL,
  PRIMARY KEY (id),
  INDEX fk_airport_country1_idx (country_id ASC) VISIBLE,
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
  CONSTRAINT fk_airport_country1
    FOREIGN KEY (country_id)
    REFERENCES mydb.country (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.airport_waypoint
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.airport_waypoint (
  airport_id INT NOT NULL,
  waypoint_id INT NOT NULL,
  PRIMARY KEY (airport_id, waypoint_id),
  INDEX fk_airport_waypoint_airport_idx (airport_id ASC) VISIBLE,
  INDEX fk_airport_waypoint_waypoint_idx (waypoint_id ASC) VISIBLE,
  CONSTRAINT fk_airport_waypoint_airport
    FOREIGN KEY (airport_id)
    REFERENCES mydb.airport (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_airport_waypoint_waypoint
    FOREIGN KEY (waypoint_id)
    REFERENCES mydb.waypoint (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.airline
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.airline (
  id INT NOT NULL,
  name VARCHAR(50) NULL,
  website VARCHAR(50) NULL,
  airline_code VARCHAR(3) NULL,
  headquarters_location VARCHAR(45) NULL,
  airport_id INT NOT NULL,
  PRIMARY KEY (id),
  INDEX fk_airline_airport1_idx (airport_id ASC) VISIBLE,
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
  CONSTRAINT fk_airline_airport1
    FOREIGN KEY (airport_id)
    REFERENCES mydb.airport (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.aircraft
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.aircraft (
  id INT NOT NULL,
  name VARCHAR(20) NULL,
  total_flight INT NULL,
  registration_info_id INT NOT NULL,
  type_id INT NOT NULL,
  airline_id INT NOT NULL,
  PRIMARY KEY (id),
  INDEX fk_aircraft_registration_info1_idx (registration_info_id ASC) VISIBLE,
  INDEX fk_aircraft_type1_idx (type_id ASC) VISIBLE,
  INDEX fk_aircraft_airline1_idx (airline_id ASC) VISIBLE,
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
  CONSTRAINT fk_aircraft_registration_info1
    FOREIGN KEY (registration_info_id)
    REFERENCES mydb.registration_info (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_aircraft_type1
    FOREIGN KEY (type_id)
    REFERENCES mydb.type (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_aircraft_airline1
    FOREIGN KEY (airline_id)
    REFERENCES mydb.airline (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.role
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.role (
  id INT NOT NULL,
  name VARCHAR(20) NULL,
  role_description VARCHAR(100) NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.person
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.person (
  id INT NOT NULL,
  name VARCHAR(30) NULL,
  surname VARCHAR(30) NULL,
  standing INT NULL,
  employee_id INT NULL,
  role_id INT NOT NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
  INDEX fk_person_role1_idx (role_id ASC) VISIBLE,
  CONSTRAINT fk_person_role1
    FOREIGN KEY (role_id)
    REFERENCES mydb.role (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.crew
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.crew (
  person_id INT NOT NULL,
  aircraft_id INT NOT NULL,
  PRIMARY KEY (person_id, aircraft_id),
  INDEX fk_crew_person1_idx (person_id ASC) VISIBLE,
  INDEX fk_crew_aircraft1_idx (aircraft_id ASC) VISIBLE,
  CONSTRAINT fk_crew_person1
    FOREIGN KEY (person_id)
    REFERENCES mydb.person (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_crew_aircraft1
    FOREIGN KEY (aircraft_id)
    REFERENCES mydb.aircraft (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.flight
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.flight (
  id INT NOT NULL,
  aircraft_id INT NOT NULL,
  departure_datetime DATETIME NULL,
  arrival_datetime DATETIME NULL,
  status ENUM('happened', 'will happen', 'is happening') NULL,
  PRIMARY KEY (id),
  INDEX fk_flight_aircraft1_idx (aircraft_id ASC) VISIBLE,
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
  CONSTRAINT fk_flight_aircraft1
    FOREIGN KEY (aircraft_id)
    REFERENCES mydb.aircraft (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.flight_route
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.flight_route (
  id INT NOT NULL,
  distance_km INT NULL,
  route_description VARCHAR(100) NULL,
  flight_id INT NOT NULL,
  PRIMARY KEY (id),
  INDEX fk_flight_route_flight1_idx (flight_id ASC) VISIBLE,
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE,
  CONSTRAINT fk_flight_route_flight1
    FOREIGN KEY (flight_id)
    REFERENCES mydb.flight (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.waypoint
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.waypoint (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NULL,
  latitude DECIMAL(10, 6) NULL,
  longitude DECIMAL(10, 6) NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table mydb.flight_waypoint
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mydb.flight_waypoint (
  flight_id INT NOT NULL,
  waypoint_id INT NOT NULL,
  waypoint_order INT NOT NULL,
  PRIMARY KEY (flight_id, waypoint_id),
  INDEX fk_flight_waypoint_flight_idx (flight_id ASC) VISIBLE,
  INDEX fk_flight_waypoint_waypoint_idx (waypoint_id ASC) VISIBLE,
  CONSTRAINT fk_flight_waypoint_flight
    FOREIGN KEY (flight_id)
    REFERENCES mydb.flight (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_flight_waypoint_waypoint
    FOREIGN KEY (waypoint_id)
    REFERENCES mydb.waypoint (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
