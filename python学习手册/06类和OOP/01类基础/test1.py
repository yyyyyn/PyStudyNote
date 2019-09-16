#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class A1:
    z = 'a1 z'

class C2(A1):
    x = 'c2 x'
    y = 'c2 y'

class C3:
    w = 'c3 w'
    y = 'c3 y'
    z = 'c3 z'

class C1(C3, C2):
    def show_x(self):
        print(self.z)

l1 =C1()
l1.show_x()