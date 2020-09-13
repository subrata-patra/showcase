mysql> SELECT COUNT(*), movies.name FROM movies_comments AS mc JOIN comments ON mc.comments_id = comments.id JOIN movies ON mc.movies_id = movies.id GROUP BY movies.name;
+----------+------+
| COUNT(*) | name |
+----------+------+
|        2 | DDLJ |
|        2 | DTPH |
|        2 | K3G  |
+----------+------+
3 rows in set (0.00 sec)

mysql>

