#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def deco(func):
    def wrapper(*pargs, **kargs):
        print("Wrap start")
        func(*pargs, **kargs)
        print("wrap end")
    return wrapper

@deco
def foo(x):
    print("I am in func foo")
    print("I have a pram:", x)

@deco
def foo(x, a=10):
    print("I am in func foo")
    print("I have a pram:", x, a)

foo('abc')