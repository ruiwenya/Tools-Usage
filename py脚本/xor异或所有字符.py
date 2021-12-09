import string
from base64 import *

flag = ''
codestr = b64decode('AAoHAR1TIiIkUFUjUFQgVyInVSVQJVFRUSNRX1YgXiJSVyJQVRs=')
for char in string.printable:
    for num in codestr:
        flag += chr(ord(char)^num)
    print(flag)
