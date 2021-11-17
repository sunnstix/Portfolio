PRAGMA foreign_keys = ON;
-- Table for future scalable web app
-- CREATE TABLE users (
--     username VARCHAR(32) PRIMARY KEY,
--     fullname VARCHAR(40) NOT NULL,
--     email VARCHAR(40) NOT NULL,
--     password VARCHAR(256) NOT NULL,
--     created DATETIME DEFAULT CURRENT_TIMESTAMP
-- );
CREATE TABLE Background (
    username VARCHAR(32) PRIMARY KEY,
    aboutme VARCHAR(2048),
    prospect VARCHAR (256),
    fullname VARCHAR(128) NOT NULL,
    age INTEGER NOT NULL,
    email VARCHAR(256) NOT NULL,
    github VARCHAR(256) NOT NULL,
    linkedin VARCHAR(256) NOT NULL
);
CREATE TABLE Skills (
    username VARCHAR(20) PRIMARY KEY,
    skill VARCHAR(256),
    strength INTEGER
);
CREATE TABLE WorkExp (
    username VARCHAR(20) PRIMARY KEY,
    title VARCHAR(64) NOT NULL,
    started DATETIME NOT NULL,
    ended DATETIME,
    company VARCHAR(64) NOT NOT NULL,
    description VARCHAR(1028) NOT NULL
);
CREATE TABLE Education (
    username VARCHAR(20) PRIMARY KEY,
    degree VARCHAR(64) NOT NULL,
    started DATETIME NOT NULL,
    ended DATETIME,
    institution VARCHAR(64) NOT NOT NULL,
    description VARCHAR(1028) NOT NULL
);
CREATE TABLE Projects (
    username VARCHAR(20) PRIMARY KEY,
    brief VARCHAR(1028),
    icon VARCHAR(128) NOT NULL,
    image VARCHAR(128) NOT NULL,
    link VARCHAR(128) NOT NULL,
    description VARCHAR(2056),
    tags VARCHAR(128)
);
CREATE TABLE Courses (
    username VARCHAR(20) PRIMARY KEY,
    brief VARCHAR(1028),
    description VARCHAR(2056),
    tags VARCHAR(128),
    institution NOT NULL,
    link VARCHAR(128)
);
CREATE TABLE Stats(
    username VARCHAR(20) PRIMARY KEY,
    stat INTEGER NOT NULL,
    name VARCHAR(64) NOT NULL
);