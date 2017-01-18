#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

print('Print step 1')
print(list(filter(is_odd, [1,2,3,4,5,6,7,9,10,15])))

#Because int make The result Ture all the time
#So script follow will return a list with no change
print('Print step 2')
print(list(filter(int,[1,2,3,4,5,6,7,8])))

def not_empty(s):
    return s and s.strip()
print('Print step 3')
print(list(filter(not_empty, ['A','','B',None,'C',' '])))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()    # list initialization
    while True:
        n = next(it)    # return first number in list
        yield n
        it = filter(_not_divisible(n), it)  # make new list

for n in primes():
    if n < 31:
        print(n)
    else:
        break

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

output = filter(is_palindrome, range(1,1000))
print('Print step 4')
print(list(output))
