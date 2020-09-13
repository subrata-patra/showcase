mysql> SELECT COUNT(student.name) as male_students FROM student JOIN class ON student.class_id = class.id JOIN teacher ON class.teacher_id = teacher.id WHERE teacher.name = 'amamika' and student.gender = 'M';
Empty set (0.00 sec)

mysql>