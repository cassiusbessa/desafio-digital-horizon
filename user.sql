CREATE TABLE
    IF NOT EXISTS users(
        id serial primary key,
        fullname varchar(255) not null,
        email varchar(255) not null,
        password varchar(255) not null,
        created_at timestamp not null
    );

CREATE DATABASE postgres_test;