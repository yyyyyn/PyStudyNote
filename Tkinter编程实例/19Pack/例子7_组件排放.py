# -*- coding: cp936 -*-
# side：改变组件的放置位置
from tkinter import *
root = Tk()
# 改变 root 的大小为 80x80
root.geometry('80x80+0+0')
print(root.pack_slaves())
# 创建三个 Label 分别使用不同的 fill 属性,改为水平放置
# 将第一个 Label 居左放置
Label(root,
text = 'pack1',
bg = 'red').pack(fill = Y,expand = 1,side = LEFT)
# 将第二个 Label 居右放置
Label(root,
text = 'pack2',
bg = 'blue').pack(fill = BOTH,expand = 1,side = RIGHT)
# 将第三个 Label 居左放置，靠 Label 放置，注意它不会放到 Label1 的左边
Label(root,
text = 'pack3',
bg = 'green').pack(fill = X,expand = 0,side = LEFT)
print(root.pack_slaves())
root.mainloop()