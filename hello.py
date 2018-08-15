#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = input()
print('hello world!', name)

print(r'\\\t\\')

print('''line1
line2
line3''')

a = 'ABC'
b = a
a = 'XYZ'
print('b', b)

print('包含中文的str')

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])

# 打印Python:
print(L[1][1])

# 打印Lisa
print(L[2][2])
