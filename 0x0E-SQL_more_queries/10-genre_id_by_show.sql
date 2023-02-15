-- script that lists all shows in hbtn_0d_tvshows that have one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id=tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
