-- List of the top 5 Chadwich Boseman movies, in order highest to lowest
SELECT
  title
FROM
  movies
  JOIN ratings ON id = ratings.movie_id
WHERE
  id IN (
    SELECT
      movie_id
    FROM
      stars
    WHERE
      person_id IN (
        SELECT
          id
        FROM
          people
        WHERE
          name = 'Chadwick Boseman'
      )
  )
ORDER BY
  ratings.rating DESC
LIMIT
  5;