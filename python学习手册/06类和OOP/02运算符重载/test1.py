#!/usr/bin/evn python
# -*- coding: UTF-8 -*-

class LoadMethod:

    def __sub__(self, other):
        "重载运算符减号，使类实例支持减法运算"
        class_name = self.__class__.__name__
        return eval('%s(self.data - other)'%(class_name))

    def gather_attrs(self):
        attrs = []
        d = self.__dict__
        for k in sorted(self.__dict__):
            attrs.append('%s=%s' % (k, getattr(self, k)))
        return ', '.join(attrs)

    def __str__(self):
        "提供打印类实例的重载方法__str__,适用于其所有子类"
        return '[%s: %s]' % (self.__class__.__name__, self.gather_attrs())

    def __getitem__(self, item):
        "查询实例属性是字典的contents对应的items项的值，不满足返回None"
        if 'contents' in self.__dict__.keys() and isinstance(self.contents, dict) and item in self.contents:
            return self.contents[item]
        else:
            return None

    def __setitem__(self, key, value):
        "查询实例属性是字典的contents并修改其中的键值对，不满足条件时提示"
        if 'contents' in self.__dict__.keys() and isinstance(self.contents, dict):
            self.contents[key] = value
        else:
            print('Nothing changed!')

class Number(LoadMethod):
    def __init__(self, start, contents={}):
        self.data = start
        self.contents = contents

if __name__ == '__main__':
    n1 = Number(4,{'a':1})
    n1['b'] = 12
    print(n1['a'], n1['b'])
    n2 = n1 - 2
    print(n2)