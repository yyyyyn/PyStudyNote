'''
处理目录都尽量用所给方法来处理，这样可以适用于不同操作系统
'''
import os
print('os.name','->',os.name)
print(os.environ)               #操作系统所有的环境变量
print(os.environ.get('PATH'))   #查找环境变量'PATH'的值

print('--------------------')
print(os.path.abspath('.'))     #查看当前目录的绝对路径
newpath=os.path.join(os.path.abspath('.'),'testdir')    #拼接地址目录
print(newpath,type(newpath))
#os.mkdir(newpath)               #创建一个目录
#os.rmdir(newpath)              #删掉一个目录
print(os.path.split('/a/b.txt'))    #拆分目录，可以得到最后的文件名称
print(os.path.splitext('/a/b.txt')) #拆分目录，可以得到最后的文件后缀

print(os.listdir('.'))              #当前目录下所有目录及文件
L=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(L)
L=[x for x in os.listdir('.') if os.path.splitext(x)[0]=='test']
for i in L:
    os.remove(i)

f=open('test.txt','w')
f.close()
os.rename('test.txt','test.py')     #重命名
print(type(os.listdir('.')),[x for x in os.listdir('.') if os.path.splitext(x)[0]=='test'])
os.remove('test.py')                #删除文件