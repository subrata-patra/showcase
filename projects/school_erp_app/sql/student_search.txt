mysql> SELECT * FROM student JOIN teacher ON student.teacher_id = teacher.id WHERE teacher.name = 'raj';
+----+--------+------------+----------+------------+----+------+
| id | name   | teacher_id | class_id | section_id | id | name |
+----+--------+------------+----------+------------+----+------+
|  5 | sadhna |          2 |        1 |          3 |  2 | raj  |
+----+--------+------------+----------+------------+----+------+
1 row in set (0.00 sec)

mysql> SELECT * FROM student JOIN section ON student.section_id = section.id JOIN teacher ON section.teacher_id = teacher.id WHERE teacher.name = 'laxmi';
+----+--------+------------+----------+------------+----+------+------------+----+-------+
| id | name   | teacher_id | class_id | section_id | id | name | teacher_id | id | name  |
+----+--------+------------+----------+------------+----+------+------------+----+-------+
|  5 | sadhna |          2 |        1 |          3 |  3 | C    |          3 |  3 | laxmi |
+----+--------+------------+----------+------------+----+------+------------+----+-------+
1 row in set (0.00 sec)

mysql> 