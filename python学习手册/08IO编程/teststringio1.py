'''
StringIO:在内存中读写字符串
BytesIO:在内存中读写二进制数据
'''
from io import StringIO,BytesIO

f=StringIO()
f.write('hello stringio')
print(f.getvalue())

f=BytesIO()
f.write('你好，中国!'.encode('utf-8'))
print(f.getvalue())
print(f.getvalue().decode('utf-8'))