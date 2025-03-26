add_movies = """
INSERT INTO movies
    (name, description, rating)
VALUES
    ('slunce seno', 'blazniva komedie', 8),
    ('leon', 'krimi', 8),
    ('matrix', 'sci-fi', 9),
    ('brat', 'dram', 9),
    ('Wall-E', 'dram', 6)
;
"""

add_tickets = """
INSERT INTO tickets
    (quantity, price)
VALUES
    (4, 8),
    (1, 10),
    (1, 16),
    (1, 14)
;
"""

select_movies = """
SELECT * FROM movies
WHERE name LIKE 'W%';
"""

select_tickets1 = """
SELECT * FROM tickets 
WHERE price > 15.30;
"""

select_tickets2 = """
SELECT * FROM tickets
WHERE quantity > 3;
"""



