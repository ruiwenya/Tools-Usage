import struct
import binascii
import os
 
# https://blog.csdn.net/zhangchilei/article/details/106563113
# print(binascii.crc32(b"hello world"))
# # Or, in two pieces:
# crc = binascii.crc32(b"hello")
# crc = binascii.crc32(b" world", crc)
# print('crc32 = {:#010x}'.format(crc))


m = open("tmp/18.png", "rb").read()
k = 0
for i in range(5000):
    if k == 1:
        break
    for j in range(5000):
        c = m[12:16] + struct.pack('>i', i) + struct.pack('>i', j)+m[24:29]
        crc = binascii.crc32(c) & 0xffffffff
        if crc == 0xab212a35:
            k = 1
            print(hex(i), hex(j))
            break

