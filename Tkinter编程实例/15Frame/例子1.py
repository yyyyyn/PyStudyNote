# width：指定宽度
# height：指定高度
# fg：指定前景色
# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
root.geometry('600x400')
#以不同的颜色区别各个 frame
for fm in ['red','blue','yellow','green','white','black']:
#注意这个创建 Frame 的方法与其它创建控件的方法不同，第一个参数不是 root
    Frame(height = 20,width = 400,bg = fm).pack()
root.mainloop()
#添加不同颜色的 Frame，大小均为 20*400