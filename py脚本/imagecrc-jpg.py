import zlib
import struct
filename = "tmp/9-14image1.jpeg"
with open(filename, 'rb') as f:
    all_b = f.read()
    #w = all_b[159:161]
    #h = all_b[157:159]
    for i in range(901,1200):
        name = str(i) + ".jpg"
        f1 = open("tmp/ctfshowmisc/tmp/"+name,"wb")
        im = all_b[:159]+struct.pack('>h',i)+all_b[161:]
        f1.write(im)
        f1.close()

# 原理一样

# import struct
# import zlib
# #爆破jpg宽度
# f = open('tmp/ctfshowmisc/misc35.jpg','rb')
# c = f.read()
# # width = c[c.index(b'\x00\x96\x03\x84')+2:c.index(b'\x00\x96\x03\x84')+4]
# # height = c[c.index(b'\x00\x96\x03\x84'):c.index(b'\x00\x96\x03\x84')+2]
# for i in range(900,1000):
#     f1 = open('tmp/ctfshowmisc/tmp/'+str(i)+'.jpg','wb')
#     # print(struct.pack('>i',i)[::-1])
#     img = c[:c.index(b'\x02\x96\x03\x84')+2]+struct.pack('>h',i)+c[c.index(b'\x02\x96\x03\x84')+4:]
#     f1.write(img)
#     f1.close()


