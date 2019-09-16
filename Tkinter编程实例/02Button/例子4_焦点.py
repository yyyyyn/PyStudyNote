from tkinter import  *
r=Tk()
def btn1():
    print('button1 clicked!')
def btn2(event):
    print('button2 clicked!')
def btn3():
    print('button3 clicked!')

b1=Button(r,text='button1',command=btn1)
b2=Button(r,text='button2')
b2.bind("<Key>",btn2)
b3=Button(r,text='button3',command=btn3)
b1.pack()
b2.pack()
b3.pack()
b1.focus_set()
r.mainloop()
