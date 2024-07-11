-- SQL script to create a trigger that decreases item quantity after adding a new order
-- Task: Create a trigger in MySQL that automatically decreases the quantity of an item in the `items` table after adding a new order.

DELIMITER //

CREATE TRIGGER after_insert_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END//

DELIMITER ;
