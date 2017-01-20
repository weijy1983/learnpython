#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'code from www.liaoxuefeng.com'

__author__='Weijy'

def foo(s):
    try:
        print(10/s)
    except ZeroDivisionError as e:
        print('There are an Error occured:',e)
    finally:
        print('finally...')

print('End')        
