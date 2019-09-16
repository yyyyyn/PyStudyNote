'''
图像与文本
'''
from tkinter import *
root=Tk()
root.title='图像与文本'
root.geometry('600x400')
Label(root,
      text='label1',
      bitmap='error',
      compound='left').pack()

root.mainloop()