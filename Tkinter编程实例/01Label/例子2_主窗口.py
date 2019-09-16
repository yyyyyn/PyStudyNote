'''
Tk()是根窗口，其部分属性如下
'''
from tkinter import *

root = Tk()

root['height'] = 300                     #设置高
root['width'] = 500                      #设置宽
root.title('魔方小站')                    #设置标题
root['bg'] = '#0099ff'                   #设置背景色
root.geometry('500x300')                 #设置窗口大小  是x不是*
root.geometry("500x300+120+100")         #设置窗口大小  并初始化桌面位置
root.resizable(width=False,height=True)  #宽不可变 高可变  默认True
root.minsize(300,600)                    #窗口可调整的最小值
root.maxsize(600,1200)                   #窗口可调整的最大值
#root.attributes("-toolwindow", 1)        #工具栏样式
#root.attributes("-topmost", -1)          #置顶窗口
#root.state("zoomed")                     #窗口最大化
#root.iconify()                           #窗口最小化
#root.attributes("-alpha",1)              #窗口透明化 透明度从0-1，1是不透明，0是全透明
# root.iconbitmap('c:\\logo.ico')          #设置左上角图标


root.mainloop()