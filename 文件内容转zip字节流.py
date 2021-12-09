import struct

a = open("flag.txt","r")#十六进制数据文件
lines = a.read()
res = [lines[i:i+2] for i in range(0,len(lines),2)]

with open("data.zip","wb") as f:
	for i in res:
		s = struct.pack('B',int(i,16))
		f.write(s)
