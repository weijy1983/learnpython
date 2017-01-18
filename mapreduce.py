#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from functools import reduce

def f(x):
	return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print('Print step 1')
print(list(r))

print('Print step 2')
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

def fn(x,y):
    return x * 10 +y

print('Print step 3') 
print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
    return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print('Print step 4')
print(reduce(fn, map(char2num,'13579')))

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

print('Print ex1')
print(L2)

def fs(x,y):
    return x * y
    
def prod(L):
    return reduce(fs, L)

print('Print ex2')
print('\'3 * 5 * 7 * 9 = \'', prod([3,5,7,9]))

def str2float(s):
    def fn(x,y):
        return x * 10 + y
    n = s.index('.')
    s = s[:n] + s[n+1:]
    return reduce(fn, map(int, s))/10**(len(s)-n)

print('Print ex3')
print('str2float(\'123.4567\') = ', str2float('123.4567'))
