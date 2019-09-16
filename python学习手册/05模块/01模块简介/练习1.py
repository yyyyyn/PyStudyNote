import sys,pprint
import test1

"要导入主程序目录文件test中的模块test1.py，可以用如下修改.pth方式添加路径，执行一次即可"
#f=open(r'C:\Users\Administrator\AppData\Roaming\Python\Python36\site-packages\pywin32.pth','a')
#f.writelines(r'D:\python\program\python学习\python学习手册\05模块\01模块简介\test')
#f.close()
pprint.pprint(sys.path)
print('*****************')
for i in open(r'C:\Users\Administrator\AppData\Roaming\Python\Python36\site-packages\pywin32.pth'):
    print(i,end='')
