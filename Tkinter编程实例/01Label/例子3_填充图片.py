'''
bitmap:只能指定显示的内置位图，
image:显示指定的图片，可以是本地个人图片，也可以是内置位图
'''

from tkinter import *
root=Tk()
root.title('Label使用内置位图')
root.geometry('500x600')
#Label的内容使用内置位图
Label(root,bitmap='gray12').pack()  #只显示内置位图
Label(root,bitmap='gray25').pack()
Label(root,bitmap='gray50').pack()
Label(root,bitmap='gray75').pack()

Label(root,bitmap='warning',text='warning').pack()  #显示位图与内容，未设置位置关系，默认为None，图片覆盖文字内容
Label(root,text='error',bitmap='error', compound='right').pack()    #设置文字内容，位图及两者位置关系
Label(root,text='hourglass',bitmap='hourglass', compound='left').pack()
Label(root,text='info',bitmap='info', compound='top').pack()
Label(root,text='questhead',bitmap='questhead', compound='bottom').pack()
Label(root,text='question',bitmap='question', compound='center').pack()


bm=PhotoImage(file='test.png')
#显示自己的图片，不能显示jpg格式图片
Label(root,image=bm,text='我的图片:',compound='right').pack()

root.mainloop()
