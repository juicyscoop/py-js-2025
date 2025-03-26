# vytvarime tabulky do databaze cinemas_db

create_cinemas_table = """
CREATE TABLE cinemas 
(
    id serial,
    name varchar(255),
    address varchar(255),
    PRIMARY KEY (id)
);
"""

create_movies_table = """
CREATE TABLE movies
(
    id serial,
    name varchar(100),
    description text,
    rating int,
    PRIMARY KEY (id)
);
"""

create_tickets_table = """
CREATE TABLE tickets
(
    id serial,
    quantity int,
    price real,
    PRIMARY KEY (id)
);
"""

create_payments_table = """
CREATE TABLE payments
(
    id serial,
    type varchar(100),
    date date, 
    PRIMARY KEY (id)
);
"""

# date: YYYY-MM-DD
# ALTER TABLE old_name RENAME TO new_name
# ALTER TABLE cinemas
# ALTER COLUMN column_name TYPE new_data_type INTEGER column_name::INTEGER