mysql> INSERT INTO movies (name, user_id) VALUES ('DDLJ', 1), ('DTPH', 2), ('K3G', 3);
Query OK, 3 rows affected (0.20 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM movies;
+----+------+---------+
| id | name | user_id |
+----+------+---------+
|  1 | DDLJ |       1 |
|  2 | DTPH |       2 |
|  3 | K3G  |       3 |
+----+------+---------+
3 rows in set (0.00 sec)

mysql> 