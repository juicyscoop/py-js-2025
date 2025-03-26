create_products_table = """
CREATE TABLE products
    (
        id serial,
        name varchar(255),
        description text,
        price decimal(5, 2),
        PRIMARY KEY(id)
    );
"""

create_orders_table = """
CREATE TABLE orders
    (
        id serial,
        description text,
        PRIMARY KEY (id)
    );
"""

create_customers_table = """
CREATE TABLE customers
    (
        id serial,
        name varchar(255),
        surname varchar(255),
        PRIMARY KEY (id)
    );
"""

