mysql> INSERT INTO teacher (name) VALUES ('amamika'), ('raj'), ('laxmi');
Query OK, 3 rows affected (0.36 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM teacher;
+----+---------+
| id | name    |
+----+---------+
|  1 | amamika |
|  2 | raj     |
|  3 | laxmi   |
+----+---------+
3 rows in set (0.02 sec)

mysql> 