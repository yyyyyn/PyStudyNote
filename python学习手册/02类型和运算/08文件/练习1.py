import os

if not os.path.exists(r'testfile/test.txt'):
    f=open(r'testfile/test.txt','w')
    f.close()

f=open(r'testfile/test.txt','w')
f.write('abc\n')
f.writelines('def\n')
f.writelines('asdf\n')
f.flush()
f.close()

print('文件迭代查询')
for line in open(r'testfile/test.txt'):
    print(line,end='')

print('文件上下文管理器')
with open(r'testfile/test.txt') as f:
    for line in f:
        print(line,end='')