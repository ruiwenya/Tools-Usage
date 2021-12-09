#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

x = 200
y = 200
im = Image.new('RGB', (x, y))
with open('qrr.txt') as f:
    for i in range(x):
        for j in range(y):
            line = f.readline()
            s = line.split(',')
            im.putpixel((i, j), (int(s[0]), int(s[1]), int(s[2])))
im.save('rgb.jpg')
