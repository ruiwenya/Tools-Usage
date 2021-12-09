# import zlib
# import struct
# filename = "tmp/ctfshowmisc/misc34.png"
# with open(filename, 'rb') as f:
#     all_b = f.read()
#     #w = all_b[159:161]
#     #h = all_b[157:159]
#     for i in range(901,1200):
#         name = str(i) + ".png"
#         f1 = open("tmp/ctfshowmisc/tmp/"+name,"wb")
#         im = all_b[:159]+struct.pack('>h',i)+all_b[161:]
#         f1.write(im)
#         f1.close()

# https://blog.csdn.net/qq_30638831/article/details/80421019
# struct


import struct
import zlib
#爆破png宽度
f = open('tmp/ctfshowmisc/misc34.png','rb')
c = f.read()
width = c[16:20]
height = c[20:24]
for i in range(900,1200):
    f1 = open('tmp/ctfshowmisc/tmp/test/'+str(i)+'.png','wb')
    # print(struct.pack('>i',i)[::-1])
    img = c[:16]+struct.pack('>i',i)+c[20:]
    #print(struct.pack('>i',i))
    f1.write(img)
    f1.close()


