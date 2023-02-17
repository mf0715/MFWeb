#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ZUC.py
@Time    :   2023/1/1114:15
@Author  :   Hu RunYang
@Version :   1.0
@Contact :   hurunyang@zxcsec.com
@License :   (C)Copyright 2017-2018, Liu group-NLP-CASA
@Desc    :   None
"""
wbin = {0: '0', 1: '1'}
whex = {'0': 0x00, '1': 0x01, '2': 0x02, '3': 0x03, '4': 0x04, '5': 0x05, '6': 0x06, '7': 0x07,
        '8': 0x08, '9': 0x09, 'A': 0x0a, 'B': 0x0b, 'C': 0x0c, 'D': 0x0d, 'E': 0x0e, 'F': 0x0f}


def hexstrTohex(source):
    num = 0x00
    temp = 0x01
    for item in source[::-1]:
        num = num + temp * whex[item]
        temp = temp * 0x10
    # num = hex(num)
    return num


def numTobinstr(source):
    re = ''
    tem = source
    while tem > 1:
        re += wbin[tem % 2]
        tem //= 2
    re += wbin[tem]
    return re[::-1]


def binstrTohex(source):
    w = {'0': 0, '1': 1}
    num = 0
    temp = 1
    for item in source[::-1]:
        num = num + temp * w[item]
        temp = temp * 2
    num = hex(num)
    return num


def genIV(cou, bea, di):
    count = numTobinstr(cou)
    while len(count) < 32:
        count = '0' + count
    bearer = numTobinstr(bea)
    while len(bearer) < 5:
        bearer = '0' + bearer
    direction = wbin[di]
    iv = []
    i = 0
    while i < 16:
        if i == 0:
            x = 0
            while x < 32:
                iv.append(count[x:x + 8])
                x = x + 8
            iv.append(bearer + direction + '00')
        elif 4 < i < 8:
            iv.append('00000000')
        elif i >= 8:
            iv.append(iv[i - 8])
        i = len(iv)
    re = ''
    for i in iv:
        tem = binstrTohex(i)[2::]
        if len(tem) < 2:
            tem = '0' + tem
        re = re + tem
    return iv


ivz = '1a6f71920000000600000001'
ivz = ivz.upper()
c = hexstrTohex(ivz[0:8])
b = hexstrTohex(ivz[8:16])
d = hexstrTohex(ivz[16:24])
print(genIV(c, b, d))