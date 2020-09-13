mysql> INSERT INTO category (name, user_id, movies_id) VALUES ('UA', 1, 1), ('A', 1, 2);
Query OK, 2 rows affected (0.18 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM category;
+----+------+---------+-----------+
| id | name | user_id | movies_id |
+----+------+---------+-----------+
|  1 | UA   |       1 |         1 |
|  2 | A    |       1 |         2 |
+----+------+---------+-----------+
2 rows in set (0.00 sec)

mysql>