create_screening_table = """
CREATE TABLE screening
(
    screening_id serial,

    movie_id int NOT NULL,
    cinema_id int NOT NULL,
    datetime timestamp,

    PRIMARY KEY (screening_id),
    
    FOREIGN KEY (movie_id) 
    REFERENCES movies(id),

    FOREIGN KEY (cinema_id)
    REFERENCES cinemas(id)
)
;
"""

add_screenings = """
INSERT INTO screening
(movie_id, cinema_id, datetime)
VALUES
(2, 1, '2024-05-05 20:00:00'),
(5, 3, '2025-03-22 19:30:00')
;
"""



