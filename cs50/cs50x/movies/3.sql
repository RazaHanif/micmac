-- All movies released on or after 2018 in alpha order
SELECT
  title
FROM
  movies
WHERE
  YEAR > '2017'
ORDER BY
  title;