# -*- coding:utf-8 -*- 
s = input("input the cipher_text Enclose with quotes:")
codebook = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.", 'H': "....", 'I': "..",
            'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-",
            'R': ".-.", 'S': "...", 'T': "-", 'U': "..-", 'V': ".--", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--..",
            '1': ".----", '2': "..---", '3': "...---", '4': "....-", '5': ".....", '6': "-....", '7': "--...",
            '8': "---..", '9': "----.", '0': "-----", '.': ".━.━.━", '?': "..--..", '!': "-.-.--", '(': "-.--.",
            '@': ".--.-.", ':': "---...", '=': "-...-", '-': "-....-", ')': "-.--.-", '+': ".-.-.", ',': "--..--",
            '\'': ".----.", '_': "..--.-", '$': "...-..-", ';': "-.-.-.", '/': "-..-.", '\"': ".-..-.", }
clear = ""
cipher = ""
while 1:
    ss = s.split(" ")
    for c in ss:
        for k in codebook.keys():
            if codebook[k] == c:
                cipher += k

    print(cipher)
    break
