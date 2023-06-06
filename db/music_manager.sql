DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255) 
);

CREATE TABLE albums (
    album_name VARCHAR(255),
    album_genre VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id),
    id SERIAL PRIMARY KEY,
);