#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test_scope():
    '''测试global,nonlocal'''
    def do_local():
        spam = 'local spam'
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
    def do_global():
        global spam
        spam = 'global spam'
    spam = 'test spam'
    do_local()
    print('after do local spam:', spam)
    do_nonlocal()
    print('after do nonlocal spam', spam)
    do_global()
    # global spam
    print('after do global spam', spam)

def intersect(seq1,seq2):
    "获取序列的交集，存入列表并返回"
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

if __name__ == '__main__':
    try:
        print(spam)
    except:
        print('error')
    test_scope()
    print(spam)

    print(intersect([1,2,3], [2,3,4]))