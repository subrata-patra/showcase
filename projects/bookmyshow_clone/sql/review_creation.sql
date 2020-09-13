mysql> INSERT INTO comments (name, user_id) VALUES ('DDLJ superhit', 1), ('DTPH drama', 1), ('K3G emotional', 2);
Query OK, 3 rows affected (0.13 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM comments;
+----+---------------+---------+
| id | name          | user_id |
+----+---------------+---------+
|  1 | DDLJ superhit |       1 |
|  2 | DTPH drama    |       1 |
|  3 | K3G emotional |       2 |
+----+---------------+---------+
3 rows in set (0.00 sec)

mysql> 