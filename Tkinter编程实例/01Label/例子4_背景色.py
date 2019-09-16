'''
fg:前景色
bg:背景色
使用颜色：
1>颜色名称：red,green,blue..
2.使用#RRGGBB
3.质差与os襄垣的颜色值，不过不建议，不利于移植
'''
from tkinter import *
root=Tk()
#root.geometry("500x300+120+100")
root.geometry("600x400+400+200")
Label(root,
      fg='red',
      bg='blue',
      text='hello tkinter').pack()
Label(root,
      fg='red',
      bg='#FF00FF',
      text='hello tkinter').pack()
Label(root,
      fg='red',
      bg='SystemBUttonShadow').pack()
root.mainloop()

