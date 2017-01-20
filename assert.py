#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'code from www.liaoxuefeng.com'

import logging
logging.basicConfig(level=logging.INFO)

__author__='Weijy'

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10/n

def main():
    foo('0')

s = '0'
n = int(s)
logging.info('n = %d' %n)
print(10 / n)
