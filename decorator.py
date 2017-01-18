#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator        

@log('execute')
def now():
    print('2017-01-18')

now()    
print('This line add by master')
