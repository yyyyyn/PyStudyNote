#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__=''
"数字"
print('--------cmath--------')
import cmath
print(cmath.pi)
print(cmath.sqrt(82))

print('--------random--------')
import random
print(random.random())
print(random.choice([1,2,3,4]))

#字符串
s='spam'
print('----------字符串 分片--------')
print(len(s))
print(s[0])
print(s[-1])
print(s[len(s)-1])
print(s[1:3])
print(s[0:])
print(s[:-1])
print(s[:])
print(s[0:3:2])#对字符串s在0:3的分片基础上每间隔1个取一个(2个中取一个)

print('----------字符串 方法--------')
print('aabbcc'.find('b'))
print('abc'.replace('b','B'))

print('----------字符串 其它编写方法--------')
print('A\nB\tC') #转义字符
msg='''aaa\nbbb
ccc'''
print(msg)  #三引号,不显示转义符，只显示效果,可用于大量复杂的文本描述
print(r'd:\n.txt') #原始字符串常量，去掉了转义机制
print("ab'cd") #单引号中加双引号或双引号中加单引号，不用转义
print('abc',"abc") #双引号和单引号都可以定义字符串，效果一样

print('----------字符串 模式匹配--------')
import re #可用于正则表达式
match=re.match('hello[\t]*(.*)world','hello  python world')
print(match.group(1))