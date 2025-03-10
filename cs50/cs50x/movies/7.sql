-- All movies from 2010 and ratings in order by rating
SELECT
  title,
  rating
FROM
  movies
  JOIN ratings ON movies.id = ratings.movie_id
WHERE
  YEAR = '2010'
ORDER BY
  rating DESC,
  title;