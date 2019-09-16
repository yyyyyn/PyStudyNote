'''
wraplength： 指定多少单位后开始换行
justify: 指定多行的对齐方式
ahchor： 指定文本(text)或图像(bitmap/image)在 Label 中的显示位置
justify/anchor区别：一个控制文本多行的对齐，一个控制整个文本在label中的位置
'''
from tkinter import *
root=Tk()
Label(root,
      text='welcome to jcodeer.cublog.cn',
      bg='yellow',
      width=40,
      height=3,
      wraplength=80,
      justify='left').pack()
Label(root,
      text='welcome to jcodeer.cublog.cn',
      bg='blue',
      width=40,
      height=3,
      wraplength=80,
      anchor='w').pack()
root.mainloop()