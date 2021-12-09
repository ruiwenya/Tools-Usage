# coding: utf-8

import hashlib

dic = '0123456789qazwsxedcrfvtgbyhnujmikolp'
md5 = hashlib.md5(dic.encode('utf-8')).hexdigest()
for a in dic:
    for b in dic:
        t = str(a) + str(b)
        md5 = hashlib.md5(t.encode('utf-8')).hexdigest()
        # print md5
        # print md5[1:2]
        # print md5[14:15]
        # print md5[17:18]
        if md5[1:2] == md5[14:15] and md5[14:15] == md5[17:18]:
            print(t)
            print(md5)
            print(md5[1:2])
            print(md5[14:15])
            print(md5[17:18])
