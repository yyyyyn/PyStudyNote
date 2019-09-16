'''一个简单的Label例子'''
from tkinter import *

root=Tk()                                 #根窗口
root.title('一个简单的Label例子')
root.geometry('500x300')                 #设置窗口大小  是x不是*
#初始化Tk，建立根窗口
label=Label(root,text='label:hello tkinter')
#创建一个Label实例，属于root,内容为text
label.pack()
#打包label,要显示就必须打包,特殊的是root不需要打包
root.mainloop()
#进入消息循环

