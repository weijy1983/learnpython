#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

'code from www.liaoxuefeng.com'

__author__='Weijy'

from types import MethodType

class animal(object):
    def run(self):
        print('This animal is running')

class dog(animal):
    def run(self):
        print('This dog is eatting')

class cat(animal):
    def run(self):
        print('This cat is running')
    
    def eat(sefl):
        print('This cat can eat too')

class tortoise(animal):
    def run(self):
        print('Tortoise is running slowly...')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(animal())
run_twice(dog())
run_twice(cat())
run_twice(tortoise())

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

s = Student()
s.score = 95
print(s.score)