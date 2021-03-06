CREATE TABLE movie (
  id  serial PRIMARY KEY,
  name varchar(130) NOT NULL,
  year integer NOT NULL,
  length integer NOT NULL,
  budget integer NOT NULL
);

INSERT INTO movie (name, year, length, budget)
    VALUES
      ('How to Train Your Dragon', 2010, 98, 165000000),
      ('Up', 2009, 96, 175000000),
      ('My Neighbor Totoro', 1988, 86, 0),
      ('The Edge of Tomorrow', 2014, 113, 178000000),
      ('Godzilla', 2014, 123, 160000000);

CREATE TABLE actor (
  id  serial PRIMARY KEY,
  name varchar(130) NOT NULL,
  gender varchar(1) NOT NULL
);


INSERT INTO actor (name, gender)
    VALUES
      ('Jay Baruchel', 'M'),
      ('Gerard Butler', 'M'),
      ('Craig Ferguson', 'M'),
      ('Edward Asner', 'M'),
      ('Christopher Plummer', 'M'),
      ('Jordan Nagai', 'M'),
      ('Toshiyuki Amagasa', 'F'),
      ('Paul Butcher', 'M'),
      ('Pat Carroll', 'F'),
      ('Tom Cruise', 'M'),
      ('Emily Blunt', 'F'),
      ('Brendan Gleeson', 'F'),
      ('Aaron Taylor-Johnson', 'M'),
      ('CJ Adams', 'M'),
      ('Ken Watanabe', 'M');

CREATE TABLE director (
  id  serial PRIMARY KEY,
  name varchar(130) NOT NULL
);

INSERT INTO director (name)
    VALUES
      ('Dean DeBlois'),
      ('Pete Docter'),
      ('Hayao Miyazaki'),
      ('Doug Liman'),
      ('Gareth Edwards');

CREATE TABLE genre (
  id  serial PRIMARY KEY,
  type varchar(20) NOT NULL
);

INSERT INTO genre (type)
    VALUES
      ('Animation'),
      ('Action');

CREATE TABLE genre_movie (
  genre_id integer references genre,
  movie_id integer references movie,
  PRIMARY KEY (genre_id, movie_id)
);

INSERT INTO genre_movie (genre_id, movie_id)
    VALUES
      (1, 1),
      (1, 2),
      (1, 3),
      (2, 4),
      (2, 5);

CREATE TABLE actor_movie (
  actor_id integer references actor,
  movie_id integer references movie,
  primary key (actor_id, movie_id)
);

INSERT INTO actor_movie (actor_id, movie_id)
    VALUES
      (1, 1),
      (2, 1),
      (3, 1),
      (4, 2),
      (5, 2),
      (6, 2),
      (7, 3),
      (8, 3),
      (9, 3),
      (10, 4),
      (11, 4),
      (12, 4),
      (13, 5),
      (14, 5),
      (15, 5);

SELECT * from movie where year > 2009;

SELECT movie.id, movie.name
  FROM genre
  INNER JOIN genre_movie
  ON (genre.id = genre_movie.genre_id)
  INNER JOIN movie
  ON (genre_movie.movie_id = movie.id)
  WHERE genre.id = 1;

SELECT director.id as director_id, director.name as director_name, movie.name, movie.budget
  from director, movie
  where director.id = movie.id;

select actor.name, movie.name, movie.year from actor, movie order by movie.year asc;
