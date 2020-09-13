mysql> INSERT INTO class (name, teacher_id) VALUES ('VI', 1), ('III', 3), ('IX', 2);
Query OK, 3 rows affected (0.18 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM class;
+----+------+------------+
| id | name | teacher_id |
+----+------+------------+
|  1 | VI   |          1 |
|  2 | III  |          3 |
|  3 | IX   |          2 |
+----+------+------------+
3 rows in set (0.00 sec)

mysql> 