#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = (1, 2, 3, 4, 5, 6, 7)

print(l[2:4])

print(l[:3])

print("abcdefg"[:4])


def trim(tim_str):
    if tim_str[0:1] == " ":
        return trim(tim_str[1:])
    elif tim_str[-1:] == " ":
        return trim(tim_str[:-1])
    else:
        return tim_str


str1 = '  中国 '
print(str1)
trims = trim(str1)
print(trims)
