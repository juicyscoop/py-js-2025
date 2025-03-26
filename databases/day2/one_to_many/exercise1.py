
create_table_opinions = """
CREATE TABLE opinions 
(
    opinion_id serial,
    product_id int,
    description text,

    PRIMARY KEY (opinion_id),
    FOREIGN KEY (product_id)
    REFERENCES products(id)
)
;
"""

insert_opinions_valid = """
INSERT INTO opinions
(product_id, description)
VALUES
(2, 'Samsung je skvely!')
;
"""

insert_opinions_invalid = """
INSERT INTO opinions
(product_id, description)
VALUES
(5, 'Nokia je bozi!')
;
"""

join_products_opinions = """
SELECT * FROM opinions
JOIN
products
ON 
opinions.product_id=products.id
;
"""