-- SQL script to create an index on the first letter of the column name in the table names

-- Ensure the table exists
DROP TABLE IF EXISTS names;
CREATE TABLE IF NOT EXISTS names (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Drop the index if it already exists
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create the index on the first letter of the column name
CREATE INDEX idx_name_first ON names (name(1));

-- Insert example data into the names table
INSERT INTO names (name) VALUES ('Alice'), ('Bob'), ('Charlie'), ('Dave'), ('Eve');

-- Query using the index to check performance
SELECT COUNT(name) FROM names WHERE name LIKE 'A%';
