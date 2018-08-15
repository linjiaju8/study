#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from myAbs import my_abs
from move import move
import math

print('abs', abs(-20))

print('max', max(2, 3, 1, -5))

print('int', int(12.34))

print('my_abs', my_abs(-9))

x, y = move(100, 100, 60, math.pi / 6)

print('move', x, y)
