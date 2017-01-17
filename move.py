#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
