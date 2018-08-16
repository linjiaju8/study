#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = map(f, L)
print(list(r))

print(list(map(str, L)))


def add(x, y):
    return x * 10 + y


print(reduce(add, [1, 3, 5, 7, 9]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('2233556'))


def normalize(name):
    return name.title()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(l):
    def fn(x, y):
        return x * y

    return reduce(fn, l)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    def fn(x, y):
        if y is None:
            return x
        else:
            return x * 10 + y

    def char2num(s):
        if '.' == s:
            pass
        else:
            return DIGITS[s]

    decimal_len = len(s[s.find(".") + 1:])

    return reduce(fn, map(char2num, s)) / pow(10, decimal_len)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
