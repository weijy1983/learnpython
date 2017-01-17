#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

import math

x1 = 0
x2 = 0

def quadratic(a, b, c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    print('Result x1 is: %.2f'%x1)
    print('Result x2 is: %.2f'%x2)

   
