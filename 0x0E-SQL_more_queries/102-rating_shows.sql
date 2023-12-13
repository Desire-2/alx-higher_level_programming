-- Lists All Shows From hbtn_0d_tvshows_rate By Their Rating.
-- Records are ordered By Descending Rating.
SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
