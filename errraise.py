#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'code from www.liaoxuefeng.com'

__author__='Weijy'

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
