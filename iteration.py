#!/usr/bin/env python3
# -*- coding: utf-8 -*-

testStr = "abc!2346"

for ch in testStr:
    print("ch:", ch)

l = {'a': 1, 'b': 2, 'c': 3}
for key in l:
    print("key:", key)
    print("val:", l[key])

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print("x,y:", x, y)

testList = [1, 3, 4, 2, 9, 7, 5]


def findMinAndMax(L):
    maxVal = None
    minVal = None
    for val in L:
        if maxVal == None:
            maxVal = val
            minVal = val
        else:
            if val > maxVal:
                maxVal = val
            elif val < minVal:
                minVal = val
            else:
                pass
    return (minVal, maxVal)


print(findMinAndMax(list))

testList = []

print(findMinAndMax(list))

testList = [7]

print(findMinAndMax(list))

testList = [7, 1]

print(findMinAndMax(list))
