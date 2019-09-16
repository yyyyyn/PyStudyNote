from tkinter import *
root=Tk()
root.geometry('600x400')
fm=[]
for color in ['red','blue']:
    fm.append(Frame(root,height=200,width=600,bg=color))
    fm[-1].pack()
Label(fm[1],text='aaa').pack()
root.mainloop()