mysql> SELECT COUNT(*) as num FROM movies JOIN category ON movies.id = category.movies_id GROUP BY category.name HAVING num > 10;
Empty set (0.05 sec)

mysql> 