mysql> INSERT INTO student (name, teacher_id, class_id, section_id) VALUES ('veda', 1, 1, 2), ('sadhna', 2, 1, 3), ('adi', 3, 2, 1);
Query OK, 3 rows affected (0.17 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM student;
+----+--------+------------+----------+------------+
| id | name   | teacher_id | class_id | section_id |
+----+--------+------------+----------+------------+
|  4 | veda   |          1 |        1 |          2 |
|  5 | sadhna |          2 |        1 |          3 |
|  6 | adi    |          3 |        2 |          1 |
+----+--------+------------+----------+------------+
3 rows in set (0.00 sec)

mysql> 