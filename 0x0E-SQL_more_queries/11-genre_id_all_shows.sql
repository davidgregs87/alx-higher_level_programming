-- script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT tvs.title, it.genre_id
FROM  tv_show_genres it
RIGHT OUTER JOIN tv_shows tvs
ON it.show_id = tvs.id
ORDER BY tvs.title, it.genre_id ASC;
