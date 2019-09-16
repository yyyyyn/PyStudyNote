'''
处理BOM:
某些软件，如notepad，在保存一个以UTF-8编码的文件时，会在文件开始的地方插入三个不可见的字符
（0xEF 0xBB 0xBF，即BOM）。因此我们在读取时需要自己去掉这些字符
'''
import sys
print(sys.getdefaultencoding())
#open('test3.txt','w',encoding='utf-8').write('spam\nSPAM\n')
print(open('test3.txt','r',encoding='utf-8').read())
print(open('test3.txt','r',encoding='utf-8-sig').read())