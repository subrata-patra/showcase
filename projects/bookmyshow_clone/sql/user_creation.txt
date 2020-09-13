mysql> INSERT INTO user (name) VALUES ('subrata'), ('neel'), ('veda');
Query OK, 3 rows affected (0.89 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM user;
+----+---------+
| id | name    |
+----+---------+
|  1 | subrata |
|  2 | neel    |
|  3 | veda    |
+----+---------+
3 rows in set (0.06 sec)

mysql> 