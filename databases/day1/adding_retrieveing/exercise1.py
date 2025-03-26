# id | name | surname

add_one_row_to_customers_table = """
INSERT INTO customers (name, surname) VALUES ('honza', 'novak');
"""
add_multiple_rows_to_customers_table = """
INSERT INTO customers
    (name, surname)
VALUES 
    ('martin', 'kral'),
    ('lukas', 'novak'),
    ('jana', 'novak')
;
"""

add_multiple_rows_to_orders_table = """
INSERT INTO orders
    (description)
VALUES 
    ('objednavka 1'),
    ('objednavka 2'),
    ('objednavka 3')
;
"""

add_multiple_rows_to_products_table = """
INSERT INTO products
    (name, description, price)
VALUES
    ('iphone', 'smartphone', 900),
    ('samsung', 'galaxy', 800),
    ('xiaomi', 'redmi', 500)
;
"""