'''
import tkinter as tk
root = tk.Tk()

root.title('去哪')
root.geometry('1440x900')
root.configure(background = 'burlywood1')

root.mainloop()
'''
from tkinter import *
root = Tk()
root.configure(background = 'burlywood1')

menubar = Menu(root)
def printItem():
    print("popup menu")
filemenu = Menu(menubar,tearoff=0)
for kk in ["python","php","jave"]:
    filemenu.add_command(label=kk,command=printItem)
    filemenu.add_separator()
menubar.add_cascade(label="language",menu=filemenu)
def popup(event):
    #顯示選單
    menubar.post(event.x_root,event.y_root)
#在這裡相應滑鼠右鍵事件，右鍵呼叫popup,此時與選單繫結的是root，可以設定為其他的控制元件，在繫結的控制元件上右擊可以彈出選單
root.bind("<Button-3>",popup)
mainloop()