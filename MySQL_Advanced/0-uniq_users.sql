-- SQL script that creates a table users
-- Table creation script
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    PRIMARY KEY(id)
);
