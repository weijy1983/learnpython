#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

print('Print step 1')
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))

print('Print step 2')

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return sorted(t, key = lambda t:t[0])
 
print('Sort by name')
print(by_name(L))

def by_name(t):
    return sorted(t, key = lambda t:t[1])
 
print('Sort by scored')
print(by_name(L))
