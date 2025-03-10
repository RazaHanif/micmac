-- List of everyone who starred in a movie from 2004, in order by birth year
SELECT
  name
FROM
  people
WHERE
  id IN (
    SELECT
      person_id
    FROM
      stars
    WHERE
      movie_id IN (
        SELECT
          id
        FROM
          movies
        WHERE
          YEAR = '2004'
      )
  )
ORDER BY
  birth;