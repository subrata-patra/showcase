mysql> SELECT * FROM class JOIN student ON student.class_id = class.id JOIN section ON student.section_id = section.id WHERE class.name = 'VI' AND section.name = 'B';
+----+------+------------+----+------+------------+----------+------------+----+------+------------+
| id | name | teacher_id | id | name | teacher_id | class_id | section_id | id | name | teacher_id |
+----+------+------------+----+------+------------+----------+------------+----+------+------------+
|  1 | VI   |          1 |  4 | veda |          1 |        1 |          2 |  2 | B    |          2 |
+----+------+------------+----+------+------------+----------+------------+----+------+------------+
1 row in set (0.03 sec)

mysql> SELECT COUNT(student.name) FROM class JOIN student ON student.class_id = class.id JOIN section ON student.section_id = section.id WHERE class.name = 'VI' AND section.name = 'B';
+---------------------+
| COUNT(student.name) |
+---------------------+
|                   1 |
+---------------------+
1 row in set (0.13 sec)

mysql>