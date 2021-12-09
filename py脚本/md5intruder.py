# coding: utf-8

import hashlib

dic = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# md5 = hashlib.md5(dic.encode('utf-8')).hexdigest()
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
num2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for a in dic:
    for b in dic:
        for c in  dic:
            t = str(a) + str(b)+str(c)
            md5 = hashlib.md5(t.encode('utf-8')).hexdigest()
            if md5[1:2] == md5[14:15] and md5[14:15] == md5[17:18]:
                # print(t)
                # print(md5)
                # print(md5[1:2])
                # print(md5[14:15])
                # print(md5[17:18])
                # print(md5[31:32])
                # print("-" * 30)
                if md5[1:2] in num2 and md5[14:15] in num and md5[17:18] in num and md5[31:32] in num:
                    if (int(md5[1:2]) + int(md5[14:15]) + int(md5[17:18])) / int(md5[1:2]) == int(md5[31:32]):
                        print(t)
                        print(md5)
                        print(md5[1:2])
                        print(md5[14:15])
                        print(md5[17:18])
                        print(md5[31:32])
                        print("*" * 30)
