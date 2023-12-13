-- Lists all shows contained in The Database hbtn_0d_tvshows.
-- Displays NULL For Shows Without Genres.
-- Records Are Ordered By Ascending tv_shows.title and tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
