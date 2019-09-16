# -*- coding: cp936 -*-
#row：指定行
# column：指定列
from tkinter import *
root = Tk()
# 创建两个 Label
lb1 = Label(root,text = 'Hello',bg='red')
lb2 = Label(root,text = 'Grid',bg='yellow')
lb1.grid(row=0,column=0)
# 指定 lb2 为第一行（使用索引 0 开始），第二列（使用索引 0 开始）
lb2.grid(row = 0,column = 1)
root.mainloop()