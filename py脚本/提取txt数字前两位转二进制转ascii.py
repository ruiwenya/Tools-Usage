with open('out.txt','r') as Dec:
    res = ''
    for i in Dec.readlines():
        Bin = '{:08b}'.format(int(i))
        print(Bin)
        Sub_Bin = Bin[:-6]
        res += Sub_Bin
    print(res)

    for j in range(0,len(res),8):
        full_bin = res[j:j+8]
        print(chr(int(full_bin,2)),end="")
