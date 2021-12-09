import zlib
import struct
filename = "tmp/ctfshowmisc/misc36.gif"
with open(filename, 'rb') as f:
    all_b = f.read()
    #w = all_b[159:161]
    #h = all_b[157:159]
    for i in range(920,951):
        name = str(i) + ".gif"
        f1 = open("tmp/ctfshowmisc/tmp/"+name,"wb")
        im = all_b[:38]+struct.pack('>h',i)[::-1]+all_b[40:]
        f1.write(im)
        f1.close()

# 原理一样

# import struct
# import zlib
# #爆破gif宽度
# f = open('tmp/ctfshowmisc/misc36.gif','rb')
# c = f.read()
# # width = c[c.index(b'\x00\x96\x03\x84')+2:c.index(b'\x00\x96\x03\x84')+4]
# # height = c[c.index(b'\x00\x96\x03\x84'):c.index(b'\x00\x96\x03\x84')+2]
# for i in range(920,950):
#     f1 = open('tmp/ctfshowmisc/tmp/'+str(i)+'.gif','wb')
#     # print(struct.pack('>i',i)[::-1])
#     img = c[:c.index(b'\x00\x00\x84\x03\x2c\x01')+2]+struct.pack('>h',i)[::-1]+c[c.index(b'\x00\x00\x84\x03\x2c\x01')+4:]
#     f1.write(img)
#     f1.close()


