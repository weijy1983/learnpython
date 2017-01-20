#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'code from www.liaoxuefeng.com'

__author__='Weijy'

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('weijy tell you invalid value: %s' %s)
    return 10/n

foo('0')    
