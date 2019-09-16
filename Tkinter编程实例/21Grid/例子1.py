'''
Grid:Tkinter 参考中最推荐使用的一个布局器。实现机制是将 Widget 逻辑上
分割成表格，在指定的位置放置想要的 Widget 就可以了。
'''
# -*- coding: cp936 -*-
# grid：用来布局组件
from tkinter import *
root = Tk()
# 创建两个 Label
lb1 = Label(root,text = 'Hello')
lb2 = Label(root,text = 'Grid')
lb1.grid()
lb2.grid()
root.mainloop()
'''
grid 有两个最为重要的参数，用来指定将组件放置到什么位置，一个是 row,另一个是
column。如果不指定 row,会将组件放置到第一个可用的行上，如果不指定 column，则使用
第一列。
'''