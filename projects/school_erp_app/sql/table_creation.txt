mysql> CREATE TABLE teacher (
    -> id int NOT NULL AUTO_INCREMENT,
    -> name varchar (255) NOT NULL,
    -> PRIMARY KEY (id)
    -> );

mysql> SHOW TABLES;
+-------------------------+
| Tables_in_ww13_7db_eval |
+-------------------------+
| teacher                 |
+-------------------------+
1 row in set (0.27 sec)

mysql> DESC teacher;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(255) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
2 rows in set (0.14 sec)

mysql> CREATE TABLE class (
    -> id int NOT NULL AUTO_INCREMENT,
    -> name varchar (255) NOT NULL,
    -> teacher_id int,
    -> FOREIGN KEY (teacher_id) REFERENCES teacher (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (2.01 sec)

mysql> SHOW TABLES;
+-------------------------+
| Tables_in_ww13_7db_eval |
+-------------------------+
| class                   |
| teacher                 |
+-------------------------+
2 rows in set (0.00 sec)

mysql> DESC class;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| name       | varchar(255) | NO   |     | NULL    |                |
| teacher_id | int          | YES  | MUL | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> CREATE TABLE section (
    -> id int NOT NULL AUTO_INCREMENT,
    -> name varchar (255) NOT NULL,
    -> teacher_id int,
    -> FOREIGN KEY (teacher_id) REFERENCES teacher (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (1.24 sec)

mysql> SHOW TABLES;
+-------------------------+
| Tables_in_ww13_7db_eval |
+-------------------------+
| class                   |
| section                 |
| teacher                 |
+-------------------------+
3 rows in set (0.00 sec)

mysql> DESC section;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| name       | varchar(255) | NO   |     | NULL    |                |
| teacher_id | int          | YES  | MUL | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> CREATE TABLE student (
    -> id int NOT NULL AUTO_INCREMENT,
    -> name varchar (255) NOT NULL,
    -> teacher_id int,
    -> class_id int,
    -> section_id int,
    -> FOREIGN KEY (teacher_id) REFERENCES teacher (id),
    -> FOREIGN KEY (class_id) REFERENCES class (id),
    -> FOREIGN KEY (section_id) REFERENCES section (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (2.60 sec)

mysql> SHOW TABLES;
+-------------------------+
| Tables_in_ww13_7db_eval |
+-------------------------+
| class                   |
| section                 |
| student                 |
| teacher                 |
+-------------------------+
4 rows in set (0.07 sec)

mysql> DESC student;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| name       | varchar(255) | NO   |     | NULL    |                |
| teacher_id | int          | YES  | MUL | NULL    |                |
| class_id   | int          | YES  | MUL | NULL    |                |
| section_id | int          | YES  | MUL | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
5 rows in set (0.01 sec)

mysql> CREATE TABLE class_section (
    -> id int NOT NULL AUTO_INCREMENT,
    -> class_id int,
    -> section_id int,
    -> FOREIGN KEY (class_id) REFERENCES class (id),
    -> FOREIGN KEY (section_id) REFERENCES section (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (1.31 sec)

mysql> SHOW TABLES;
+-------------------------+
| Tables_in_ww13_7db_eval |
+-------------------------+
| class                   |
| class_section           |
| section                 |
| student                 |
| teacher                 |
+-------------------------+
5 rows in set (0.00 sec)

mysql> DESC class_section;
+------------+------+------+-----+---------+----------------+
| Field      | Type | Null | Key | Default | Extra          |
+------------+------+------+-----+---------+----------------+
| id         | int  | NO   | PRI | NULL    | auto_increment |
| class_id   | int  | YES  | MUL | NULL    |                |
| section_id | int  | YES  | MUL | NULL    |                |
+------------+------+------+-----+---------+----------------+
3 rows in set (0.07 sec)

mysql> 