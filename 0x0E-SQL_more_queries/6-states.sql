-- Creates a database that without overwriting existing versions
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switches the active database
USE hbtn_0d_usa;
-- Creates a table with a column 
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id)
);
