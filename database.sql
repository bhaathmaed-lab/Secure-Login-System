database.sql
-- Secure Login System Database

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Example user record
-- Password should be stored as a hash, not plain text

INSERT INTO users (username, email, password)
VALUES (
    'admin',
    'admin@example.com',
    'hashed_password_here'
);