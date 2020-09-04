# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email       : lunar_ubuntu@qq.com
# > Create Time: Thu 03 Sep 2020 11:03:39 PM CST

from PIL import Image
import sys

def convert(file_path, color, out):
    img = Image.open(file_path)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel = img.getpixel((i,j))
            if abs(pixel[0] - 11) <= 50 and abs(pixel[1] - 143) <= 50 and abs(pixel[2] - 130) <= 50:
                img.putpixel((i,j), color)
    img.save(out)

if __name__ == "__main__":
    convert(sys.argv[1],(255, 222, 173, 1), sys.argv[2])

