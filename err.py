#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'code from www.liaoxuefeng.com'

__author__='Weijy'

import logging

def foo(s):
    try:
        print(10/s)
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')

    print('END')        

print('End')        
