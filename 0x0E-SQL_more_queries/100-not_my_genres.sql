-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT tvg.name
FROM tv_genres tvg
INNER JOIN tv_show_genres it
ON tvg.id = it.genre_id
INNER JOIN tv_shows tvs
ON tvs.id = it.show_id
WHERE tvg.name NOT IN (
      SELECT tvg.name FROM tv_genres tvg
      INNER JOIN tv_show_genres it
      ON tvg.id = it.genre_id
      INNER JOIN tv_shows tvs
      ON tvs.id = it.show_id
      WHERE title = 'Dexter')
-- GROUP BY tvg.name
ORDER BY tvg.name ASC;
