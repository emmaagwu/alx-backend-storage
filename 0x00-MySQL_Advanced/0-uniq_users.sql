-- Script to create a table named 'users' with specified attributes

-- CREATE TABLE IF NOT EXISTS to ensure the script doesn't fail if the table already exists

CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255)
)