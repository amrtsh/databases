
CREATE TABLE IF NOT EXISTS passenger (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(54) NULL DEFAULT NULL,
  flight_id INT NOT NULL,
  PRIMARY KEY (id)
  );
  
DELIMITER //
CREATE TRIGGER passenger_flight_check
    BEFORE INSERT ON passenger
    FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM flight WHERE id = NEW.flight_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Flight does not exist';
    END IF;
END;
//
DELIMITER ;

INSERT INTO passenger (name, flight_id) VALUES ('JOHN', 2)

DELIMITER //
CREATE PROCEDURE insert_into_type(IN name varchar(54))
BEGIN
	INSERT INTO type (name) VALUES (name);
END;
//
DELIMITER ;

CALL insert_into_type('carcar');
 
 DROP PROCEDURE IF EXISTS insert_into_junction_table;
DELIMITER //

CREATE PROCEDURE insert_into_junction_table (
    IN waypoint_name VARCHAR(54),
    IN airport_name VARCHAR(54)
)
BEGIN
    DECLARE waypoint_id INT;
    DECLARE airport_id INT;

    SELECT id INTO waypoint_id FROM waypoint WHERE name = waypoint_name LIMIT 1;

    SELECT id INTO airport_id FROM airport WHERE name = airport_name LIMIT 1;

    INSERT INTO airport_waypoint (waypoint_id, airport_id) VALUES (waypoint_id, airport_id);
END //

DELIMITER ;

CALL insert_into_junction_table('New York', 'John F. Kennedy International Airport');


DROP PROCEDURE IF EXISTS insert_rows_in_package;
DELIMITER //

CREATE PROCEDURE insert_rows_in_package()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
       INSERT INTO type (name) VALUES (CONCAT('type', i));
       SET i = i + 1;
    END WHILE;
END //

DELIMITER ;

CALL insert_rows_in_package();

DROP FUNCTION IF EXISTS calculate_statistic;

DELIMITER //

CREATE FUNCTION `calculate_statistic`(
  operation VARCHAR(10)
) RETURNS int
    READS SQL DATA
BEGIN
      DECLARE result DECIMAL DEFAULT 0.0;

    IF operation = 'min' THEN
        SELECT MIN(max_speed) INTO result FROM registration_info;
    ELSEIF operation = 'max' THEN
        SELECT MAX(max_speed) INTO result FROM registration_info;
    ELSEIF operation = 'avg'  THEN
        SELECT AVG(max_speed) INTO result FROM registration_info;
  ELSEIF operation = 'sum'  THEN
        SELECT SUM(max_speed) INTO result FROM registration_info;
    END IF;
    RETURN result;
END //

DELIMITER ;


DROP PROCEDURE  IF EXISTS get_avg;

DELIMITER //

CREATE PROCEDURE `get_operation`(
  IN operation VARCHAR(10)
)
BEGIN
  DECLARE result INT;
    set result = calculate_statistic(operation);
    SELECT result;
END//

DELIMITER ;

CALL get_operation('min');


DROP PROCEDURE IF EXISTS create_tables_from_column;
DROP VIEW IF EXISTS user_view;

DELIMITER //

CREATE PROCEDURE create_tables_from_column(
    IN custom_column_name VARCHAR(45),
    IN custom_table_name VARCHAR(45)
)
BEGIN
    DECLARE a INT DEFAULT 0;
    DECLARE b INT DEFAULT 0;
    DECLARE table_name VARCHAR(45);
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE num_columns INT;
    DECLARE column_list VARCHAR(255);
    DECLARE column_name VARCHAR(45);

    DECLARE zxcursor CURSOR FOR SELECT price FROM user_view;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET @query = CONCAT('CREATE OR REPLACE VIEW user_view AS SELECT ', custom_column_name, ' AS price FROM ', custom_table_name);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    OPEN zxcursor;
    my_loop: LOOP
        FETCH zxcursor INTO table_name;
        IF done THEN
            LEAVE my_loop;
        END IF;

        SET num_columns = FLOOR(1 + RAND() * 9);
    SELECT num_columns;
    SET column_list = '';
    WHILE b < num_columns DO
      SET column_name = CONCAT('column_', b + 1);
      SET column_list = CONCAT(column_list, column_name, ' INT ');
      IF b < num_columns - 1 THEN
        SET column_list = CONCAT(column_list, ', ');
      END IF;
      SET b = b + 1;
    END WHILE;
    SET b = 0;

        SET column_list = SUBSTRING(column_list, 1, LENGTH(column_list) - 1);

    SET @sql_query = CONCAT('CREATE TABLE IF NOT EXISTS ', table_name, '_', UNIX_TIMESTAMP(), ' (', column_list, ')');
    PREPARE stmt FROM @sql_query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

        DROP VIEW IF EXISTS user_view;
        SET a = a + 1;
    END LOOP my_loop;

    CLOSE zxcursor;
END //

DELIMITER ;

CALL create_tables_from_column('name', 'person');

DELIMITER //
CREATE TRIGGER prevent_modification
    BEFORE UPDATE ON airline
    FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification not allowed';
END;
//
DELIMITER ;

update airline set name='dfght' where id=1;

DELIMITER //
CREATE TRIGGER prevent_deletion
    BEFORE DELETE ON person
    FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion not allowed';
END;
//
DELIMITER ;

delete from person where id=6;

DELIMITER //
CREATE TRIGGER prevent_double_zeros
    BEFORE INSERT ON registration_info
    FOR EACH ROW
BEGIN
    IF NEW.serial_number LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid value for serial_number';
    END IF;
END;
//
DELIMITER ;


INSERT INTO registration_info (serial_number, manufacturing_date, registration_number, capacity_passengers, max_speed, fuel_capacity, last_maintenance_date) VALUES
(100, '2020-01-15', 'N12345', 180, 560, 50000, '2023-03-20');