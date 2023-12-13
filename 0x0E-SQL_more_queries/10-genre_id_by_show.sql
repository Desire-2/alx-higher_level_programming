-- Lists All Shows in hbtn_0d_tvshows Tthat Have at Least One Genre Linked.
-- Records Are Sorted By Ascending tv_shows.title and tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
