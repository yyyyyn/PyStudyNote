#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from zjtools.classtools import AttrDisplay

class Persion(AttrDisplay):
    def __init__(self, name, age=22, pay=1000):
        self.name = name
        self.age = age
        self.pay = pay
    def show_name(self):
        print(self.name)
    def raise_pay(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Persion):
    def __init__(self, name, age=30, pay=10000, cellnum='unknow'):
        Persion.__init__(self, name, age=age, pay=pay)
        self.cellnum = cellnum
    def raise_pay(self, percent, bonus=.10):
        Persion.raise_pay(self, percent + bonus)

if __name__ == '__main__':
    p1 = Persion('Bob', 23, 1000)
    p1.raise_pay(.2)
    print(p1)
    m1 = Manager('Smith', 32, 10000)
    m1.raise_pay(.2)
    print(m1)