#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print(list(range(1, 11)))

l = []
for x in range(1, 11):
    l.append(x * x)
print(l)

print([x * x for x in range(1, 11) if x % 2 == 0])

print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}

for k, v in d.items():
    print(k, '=', v)

L = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L if isinstance(s, str)])
