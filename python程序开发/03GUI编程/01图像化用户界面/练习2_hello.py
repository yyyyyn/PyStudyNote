from tkinter import Label       #1.获取组件对象,加载组件类
import  os

widget=Label(None,text='hello GUI world!')  #2.生成，创建组件类的实例
#print(help(Label))
#print(os.path)
widget.pack()                   #3.布置，打包
widget.mainloop()               #4.开始事件循环，调用主循环，显示窗口



