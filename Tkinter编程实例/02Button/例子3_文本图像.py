# compound:指定文本与图像位置关系
# bitmap：指定位图
from tkinter import *
root = Tk()
#图像居下,居上，居右，居左，文字位于图像之上
Button(root,
text = 'botton',
compound = 'bottom',
bitmap = 'error'
).pack()
Button(root,
text = 'top',
compound = 'top',
bitmap = 'error'
).pack()
Button(root,
text = 'right',
compound = 'right',
bitmap = 'error'
).pack()
Button(root,
text = 'left',
compound = 'left',
bitmap = 'error'
).pack()
Button(root,
text = 'center',
compound = 'center',
bitmap = 'error'
).pack()
#消息循环
root.mainloop()