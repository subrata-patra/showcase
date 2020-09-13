mysql> SELECT * FROM movies JOIN category ON movies.id = category.movies_id WHERE category.name = 'UA';
+----+------+---------+----+------+---------+-----------+
| id | name | user_id | id | name | user_id | movies_id |
+----+------+---------+----+------+---------+-----------+
|  1 | DDLJ |       1 |  1 | UA   |       1 |         1 |
+----+------+---------+----+------+---------+-----------+
1 row in set (0.02 sec)

mysql> SELECT * FROM movies JOIN category ON movies.id = category.movies_id JOIN user ON user.id = movies.user_id WHERE category.name = 'UA' AND user.name = 'subrata';
+----+------+---------+----+------+---------+-----------+----+---------+
| id | name | user_id | id | name | user_id | movies_id | id | name    |
+----+------+---------+----+------+---------+-----------+----+---------+
|  1 | DDLJ |       1 |  1 | UA   |       1 |         1 |  1 | subrata |
+----+------+---------+----+------+---------+-----------+----+---------+
1 row in set (0.00 sec)

mysql> 