-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tvg.name
FROM tv_genres tvg
INNER JOIN tv_show_genres it
ON tvg.id = it.genre_id
INNER JOIN tv_shows tvs
ON tvs.id = it.show_id
WHERE tvs.title = 'Dexter'
ORDER BY tvg.name ASC;
