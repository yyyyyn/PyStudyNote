# -*- coding: cp936 -*-
# x：指定 x 坐标
# y：指定 y 坐标
# anchor：指定放置位置
from tkinter import *
root = Tk()
lb = Label(root,text = 'hello Place')
# lb.place(relx = 1,rely = 0.5,anchor = CENTER)
# 使用绝对坐标将 Label 放置到(0,0)位置上
lb.place(x = 0,y = 0,anchor = NW)
#lb.pack()
root.mainloop()
# x,y 指定组件放置的绝对位置