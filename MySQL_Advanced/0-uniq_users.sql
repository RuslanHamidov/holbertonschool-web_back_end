-- SQL script that creates a table users
-- Table creation script
CREATE TABLE table (id INT NOT NULL AUTOINCREMENT PRIMARY KEY, 
                    email VARCHAR(255) NOT NULL UNIQUE,
                    name VARCHAR(255)
                    );
