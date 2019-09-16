#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class AttrDisplay:
    '''
    提供打印类实例的重载方法__str__,适用于其所有子类
    '''
    def gather_attrs(self):
        attrs = []
        d = self.__dict__
        for k in sorted(self.__dict__):
            attrs.append('%s=%s' % (k, getattr(self, k)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gather_attrs())