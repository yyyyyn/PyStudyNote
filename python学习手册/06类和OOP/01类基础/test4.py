#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# from test3 import Persion, Manager
import shelve

# bob = Persion('Bob')
# sue = Persion('Sue',pay=5000)
# tom = Manager('Tom Jones',pay=10000)
# print(bob, sue, tom)
'''
#在shelve数据库中存储对象：
import shelve
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()
'''
'''
#glob是python自己带的一个文件操作相关模块，用它可以查找符合自己目的的文件
import glob
dbf = glob.glob('person*')
print(dbf)
print(open('persondb.dir').read())
'''
#更新shelve中的对象
db = shelve.open('persondb')
print(list(db.keys()))
bob = db['Bob']
print(bob)
db.close()

class A:
    __classname = 'test'
    def show_info(myinfo):
        print('my info is ',myinfo)
A.show_info('abc')
class B(A):
    def __init__(self):
        print('this is func init in class B')

print(A.__dict__.keys())
print(B.__dict__.keys())
print(B._A__classname)