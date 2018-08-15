#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Michael'] = 90

print(d['Michael'])

d['Jack'] = 88

print(d['Jack'])

print(d.get("Jackie", "NONE"))

s = set([1, 2, 3])

print(s)

s.remove(1)

print(s)

s = set((1, 2, 3))

print(s)
