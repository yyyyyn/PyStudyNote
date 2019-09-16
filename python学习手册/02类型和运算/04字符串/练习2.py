str1=b'aaa'
print(str1,type(str1))

str2='bbb'.encode('utf-8')
print(str2,type(str2))
print(str2.decode('utf-8'))

B=b'spam'
print(B.replace(bytes('pa','ascii'),bytes('xy','ascii')))
print('abc中文'.encode('ascii',errors='ignore'))
print(bytes('abc中文','utf-8'))

s=bytearray('你好，中国!','utf-8')
print(type(s),s,s.decode('utf-8'))

print('=========文件输出编码')
s='A\xc4B\xe8C'
print(s,s.encode('latin-1'),s.encode('utf-8'))
open('latindata','w',encoding='latin-1').write(s)
print(open('latindata','rb').read())
print(open('latindata','r',encoding='latin-1').read())