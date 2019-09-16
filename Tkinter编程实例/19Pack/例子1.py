from tkinter import *
root=Tk()
print(root.pack_slaves())
Label(root,text='hello').pack()
print(root.pack_slaves())
root.mainloop()