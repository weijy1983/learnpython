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

class Screen(object):
    @property
    def width(self):
        return self._width

    @property      
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be a integer!')
        if value < 0 or value > 10000:
            raise ValueError('width must between 0 ~ 100')
        self._width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be a integer!')
        if value < 0 or value > 10000:
            raise ValueError('height must between 0 ~ 100')
        self._height = value

    @property
    def resolution(self):
        return self._width * self.height

sq = Screen()
sq.width = 5
sq.height = 6
print(sq.resolution)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1       # init two counter a and b

    def __iter__(self):
        return self                 # is a iterator, return itself
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b    # caculater next value
        if self.a > 100000:         # exit loop
            raise StopIteration()
        return self.a               # return next value            

    def __getitem__(sefl, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a            

for n in Fib():
    print(n)

f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])
