mysql> INSERT INTO section (name, teacher_id) VALUES ('A', 1), ('B', 2), ('C', 3);
Query OK, 3 rows affected (0.19 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM section;
+----+------+------------+
| id | name | teacher_id |
+----+------+------------+
|  1 | A    |          1 |
|  2 | B    |          2 |
|  3 | C    |          3 |
+----+------+------------+
3 rows in set (0.00 sec)

mysql> 