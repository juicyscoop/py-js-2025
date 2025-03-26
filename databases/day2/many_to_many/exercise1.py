link_products_orders = """
CREATE TABLE products_orders
(
    product_order_id serial,
    product_id int NOT NULL,
    order_id int NOT NULL,

    PRIMARY KEY (product_order_id),
    
    FOREIGN KEY (product_id)
    REFERENCES products(id),
    
    FOREIGN KEY (order_id)
    REFERENCES orders(id)
)
;
"""

fill_products_orders_table_valid = """
INSERT INTO products_orders
(product_id, order_id)
VALUES
(2, 1), (3, 3), (4, 2)
;
"""

fill_products_orders_table_invalid = """
INSERT INTO products_orders
(product_id, order_id)
VALUES
(2, 4)
;
"""