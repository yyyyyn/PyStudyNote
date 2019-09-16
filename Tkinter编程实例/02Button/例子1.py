from tkinter import *

root=Tk()
root.geometry('600x400')
def helloButton():
    print('hello button')
Button(root,
       text='Hello Button',
       command=helloButton).pack()
root.mainloop()