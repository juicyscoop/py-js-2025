create_customer_address_table = """
CREATE TABLE customer_address
(
    address_id serial,
    customer_id int UNIQUE,

    city varchar(255),
    street varchar(255),
    house_no varchar(255),

    PRIMARY KEY (address_id),
    FOREIGN KEY (customer_id)
    REFERENCES customers(id)
)
;
"""

insert_addresses = """
INSERT INTO customer_address
(customer_id, city, street, house_no)
VALUES
(1, 'Praha', 'Jugoslavska', '4'),
(4, 'Kolin', 'Nova', '5')
;
"""

insert_addresses_duplicate = """
INSERT INTO customer_address
(customer_id, city, street, house_no)
VALUES
(4, 'Brno', 'Hladka', '6')
;
"""