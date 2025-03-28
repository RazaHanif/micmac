-- title and release year of all Harry Potter movies in chronological order
SELECT
  title,
  YEAR
FROM
  movies
WHERE
  title LIKE 'Harry Potter%'
ORDER BY
  YEAR;