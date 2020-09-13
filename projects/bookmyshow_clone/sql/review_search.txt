mysql> SELECT * FROM comments JOIN user ON user.id = comments.user_id WHERE user.name = 'neel';
+----+---------------+---------+----+------+
| id | name          | user_id | id | name |
+----+---------------+---------+----+------+
|  3 | K3G emotional |       2 |  2 | neel |
+----+---------------+---------+----+------+
1 row in set (0.00 sec)

mysql> 