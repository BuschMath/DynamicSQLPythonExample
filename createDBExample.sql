CREATE DATABASE mydatabase;

USE mydatabase;

CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO users (id, username, password, email)
VALUES
    (1, 'Alice', 'password1', 'alice@example.com'),
    (2, 'Bob', 'password2', 'bob@example.com'),
    (3, 'Charlie', 'password3', 'charlie@example.com');
