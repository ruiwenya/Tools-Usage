import zlib
import struct

# 同时爆破宽度和高度
# bytearray原始16进制字符
# data[x+4] 爆破width
# zlib.crc32中data也类似16进制字符 crc32 x32+x26+x23+x22+x16+x12+x11+x10+x8+x7+x5+x4+x2+x+1
# https://www.cnblogs.com/yunqian2017/p/14449346.html


filename = "tmp/9-27.png"
with open(filename, 'rb') as f:
    all_b = f.read()
    data = bytearray(all_b[12:29])
    n = 4095
    for w in range(n):
        width = bytearray(struct.pack('>i', w))
        for h in range(n):
            height = bytearray(struct.pack('>i', h))
            for x in range(4):
                data[x+4] = width[x]
                data[x+8] = height[x]
            crc32result = zlib.crc32(data)
            #替换成图片的crc
            if crc32result == 0x9af1742d:
                print("宽为：", end = '')
                print(width, end = ' ')
                print(int.from_bytes(width, byteorder='big'))
                print("高为：", end = '')
                print(height, end = ' ')
                print(int.from_bytes(height, byteorder='big'))


