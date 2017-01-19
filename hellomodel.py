#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'a test module'

__author__='Weijy'

import sys

def test():
    args = sys.argv
    print('%s will run...' % args[0])
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        print(_private_1(name))
    else:
        print(_private_2(name))

if __name__=='__main__':
    test()
    greeting('chu')
