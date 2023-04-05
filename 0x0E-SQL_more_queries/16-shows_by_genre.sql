-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
SELECT tvs.title, tvg.name
FROM  tv_show_genres it
RIGHT OUTER JOIN tv_shows tvs
ON it.show_id = tvs.id
LEFT OUTER JOIN tv_genres tvg
ON it.genre_id = tvg.id
ORDER BY tvs.title, tvg.name ASC;
