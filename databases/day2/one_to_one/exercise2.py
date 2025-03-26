drop_payments_table = """
DROP TABLE payments;
"""

recreate_payments_table = """
CREATE TABLE payments
(
    payment_id serial,
    ticket_id int UNIQUE,

    type varchar(255),
    date date,

    PRIMARY KEY (payment_id),
    FOREIGN KEY (ticket_id)
    REFERENCES tickets(id)
)
;
"""

fill_payments_table = """
INSERT INTO payments
(ticket_id, type, date)
VALUES
(1, 'card', '2025-03-22'),
(2, 'cash', '2025-03-23'),
(4, 'giftcard', '2024-03-22')
;
"""