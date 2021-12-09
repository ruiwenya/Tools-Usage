from collections import Counter


f = open('tmp/download.dat', 'r')
f_read = f.read()
print(Counter(f_read))
