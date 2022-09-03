import tkinter as tk
from time import sleep
import random

win=tk.Tk()
win.geometry("200x300")
canv=tk.Canvas(scrollregion=(0,0,500,2000))
i=0

def init():
    global i
    a=random.randint(100000,999999)
    i += 20
    canv.create_text(10, i, text="hello", fill="#"+str(a))
    canv.configure(scrollregion=(0,0,500,i))
    
    canv.yview_moveto(1.0)
    
    

but=tk.Button(text="init",command=init)
but.pack()
scro=tk.Scrollbar(command=canv.yview)
canv.config(yscrollcommand=scro.set)
scro.pack(fill=tk.Y,side='right')
canv.pack()


    
    
win.update()
   
win.mainloop()