-- SQL script to create a trigger that resets valid_email when the email is changed
-- Task: Create a trigger in MySQL that resets the valid_email attribute to 0 when the email field is updated.

DELIMITER //

CREATE TRIGGER before_update_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END//

DELIMITER ;