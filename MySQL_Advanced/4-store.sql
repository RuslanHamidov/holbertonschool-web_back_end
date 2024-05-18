-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order
-- Script that performs that
DELIMITER //

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - 1;
END //

DELIMITER ;
