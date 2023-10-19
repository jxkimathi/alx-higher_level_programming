-- lists all shows, and all genres
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_idd
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
