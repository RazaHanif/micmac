-- List of all movies that star both Bradley Cooper & Jennifer Lawrence
SELECT
  title
FROM
  movies
  JOIN stars ON movies.id = stars.movie_id
  JOIN people ON stars.person_id = people.id
WHERE
  people.name = 'Bradley Cooper'
  AND title IN (
    SELECT
      title
    FROM
      movies
      JOIN stars ON movies.id = stars.movie_id
      JOIN people ON stars.person_id = people.id
    WHERE
      people.name = 'Jennifer Lawrence'
  );