mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| subrata            |
| sys                |
| ww10_2db           |
| ww10_3db           |
| ww11_2db           |
| ww11_3db           |
| ww11_4db           |
| ww9_4db            |
| ww9_5db            |
+--------------------+
12 rows in set (1.66 sec)

mysql> CREATE DATABASE ww11_6db_project
    -> ;
Query OK, 1 row affected (0.82 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| subrata            |
| sys                |
| ww10_2db           |
| ww10_3db           |
| ww11_2db           |
| ww11_3db           |
| ww11_4db           |
| ww11_6db_project   |
| ww9_4db            |
| ww9_5db            |
+--------------------+
13 rows in set (0.00 sec)

mysql> USE ww11_6db_project;
Database changed
mysql> CREATE TABLE user (
    -> id int NOT NULL AUTO_INCREMENT,
    -> name varchar (255) NOT NULL,
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (1.75 sec)

mysql> DESC user;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(255) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
2 rows in set (0.09 sec)

mysql> CREATE TABLE movies (
    -> id int NOT NULL AUTO_INCREMENT,
    -> name varchar (255) NOT NULL,
    -> user_id int,
    -> FOREIGN KEY (user_id) REFERENCES user (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (0.75 sec)

mysql> DESC movies
    -> ;
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | int          | NO   | PRI | NULL    | auto_increment |
| name    | varchar(255) | NO   |     | NULL    |                |
| user_id | int          | YES  | MUL | NULL    |                |
+---------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> CREATE TABLE category (
    -> id int NOT NULL AUTO_INCREMENT,
    -> name varchar (255) NOT NULL,
    -> user_id int,
    -> movies_id int,
    -> FOREIGN KEY (user_id) REFERENCES user (id),
    -> FOREIGN KEY (movies_id) REFERENCES movies (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (1.18 sec)

mysql> DESC category;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int          | NO   | PRI | NULL    | auto_increment |
| name      | varchar(255) | NO   |     | NULL    |                |
| user_id   | int          | YES  | MUL | NULL    |                |
| movies_id | int          | YES  | MUL | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> CREATE TABLE comments (
    -> id int NOT NULL AUTO_INCREMENT,
    -> name varchar (255) NOT NULL,
    -> user_id int,
    -> FOREIGN KEY (user_id) REFERENCES user (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (4.10 sec)

mysql> DESC comments;
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | int          | NO   | PRI | NULL    | auto_increment |
| name    | varchar(255) | NO   |     | NULL    |                |
| user_id | int          | YES  | MUL | NULL    |                |
+---------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> CREATE TABLE movies_comments (
    -> id int NOT NULL AUTO_INCREMENT,
    -> movies_id int,
    -> comments_id int,
    -> FOREIGN KEY (movies_id) REFERENCES movies (id),
    -> FOREIGN KEY (comments_id) REFERENCES comments (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (2.46 sec)

mysql> DESC movies_comments;
+-------------+------+------+-----+---------+----------------+
| Field       | Type | Null | Key | Default | Extra          |
+-------------+------+------+-----+---------+----------------+
| id          | int  | NO   | PRI | NULL    | auto_increment |
| movies_id   | int  | YES  | MUL | NULL    |                |
| comments_id | int  | YES  | MUL | NULL    |                |
+-------------+------+------+-----+---------+----------------+
3 rows in set (0.05 sec)

mysql> CREATE TABLE comments_category (
    -> id int NOT NULL AUTO_INCREMENT,
    -> comments_id int,
    -> category_id int,
    -> FOREIGN KEY (comments_id) REFERENCES comments (id),
    -> FOREIGN KEY (category_id) REFERENCES category (id),
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (1.30 sec)

mysql> DESC comments_category;
+-------------+------+------+-----+---------+----------------+
| Field       | Type | Null | Key | Default | Extra          |
+-------------+------+------+-----+---------+----------------+
| id          | int  | NO   | PRI | NULL    | auto_increment |
| comments_id | int  | YES  | MUL | NULL    |                |
| category_id | int  | YES  | MUL | NULL    |                |
+-------------+------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> 