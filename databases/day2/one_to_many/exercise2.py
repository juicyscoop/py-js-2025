create_table_comments = """
CREATE TABLE comments
(
    comment_id serial,
    movie_id int,
    content text,
    PRIMARY KEY (comment_id),
    FOREIGN KEY (movie_id)
    REFERENCES movies(id)
)
;
"""

insert_comments = """
INSERT INTO comments
(movie_id, content)
VALUES
(2, 'Skvely film.'),
(5, 'Spatny film.')
;
"""

