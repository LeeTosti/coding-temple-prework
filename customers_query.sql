-- CREATE TABLE IF NOT EXISTS customers(cust_id INT, cust_name VARCHAR(50), address VARCHAR(200));
-- INSERT INTO customers VALUES
-- 	(10001, 'Taylor Swift', '13 Folklore Lane, Philadelphia PA');
-- INSERT INTO customers VALUES
-- 	(10002, 'Stick Stickly', 'PO Box 963, New York, NY');
-- INSERT INTO customers VALUES
-- 	(10003, 'Jim Carrey', '4 Andy Kaufman Way, Great Neck, NY');
SELECT *
FROM customers
ORDER BY cust_name ASC;