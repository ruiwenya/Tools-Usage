file = open('ascii.txt', 'w')
with open('hex.txt', 'r') as f:
    h = f.read()
tem = ''
for i in range(0, len(h), 2):
    tem = '0x'+h[i]+h[i+1]
    tem = int(tem, base=16)
    print(chr(tem), end='')
    file.write(chr(tem))
file.close()
