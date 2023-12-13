-- Lists All Genres From The Database hbtn_0d_tvshows along with the number of
-- Shows Linked To Each.
-- Does Not Display Genres Without Linked shows.
-- Records Are Ordered By Descending Number of Shows Linked.
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
