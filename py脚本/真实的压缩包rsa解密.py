import gmpy2

p = 3
q = 11
e = 0x3
c = 26
n = 33
s = (p - 1) * (q - 1)
d = gmpy2.invert(e, s)
m = pow(c, d, n)

print(pow(c, d, n))
# 5
