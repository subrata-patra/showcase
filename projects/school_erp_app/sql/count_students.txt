mysql> SELECT COUNT(student.name) as no_of_students, teacher.name FROM student JOIN teacher ON student.teacher_id = teacher.id GROUP BY teacher.name;
+----------------+---------+
| no_of_students | name    |
+----------------+---------+
|              1 | amamika |
|              1 | raj     |
|              1 | laxmi   |
+----------------+---------+
3 rows in set (0.04 sec)

mysql> 