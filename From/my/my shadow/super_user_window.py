import multiprocessing as mut
from time import sleep
import tkinter as tk

PAGE=5

def show(wi,he,z,s_str):
    a=0
    win = tk.Tk()
    win.overrideredirect(True)
    furry = tk.PhotoImage(file=s_str)
    lab = tk.Label(image=furry)
    lab.pack()
    while a < 100 and a>-100:
        win.geometry("400x400+"+str(wi)+"+"+str(he+a))
        sleep(0.1)
        a += z
        win.update()
    win.mainloop()
    
pro=[]
dispro=[]
i=0
for i in range(PAGE):
    tmp = mut.Process(target=show, args=(
        i*500,i*200, 5, '/home/tom/vscode/Python/furry.gif',))
    pro.append(tmp)
    pro[i].start()
    sleep(2)
for i in range(PAGE):
    tmp = mut.Process(target=show, args=(
        i*500, i*200+100, -5, '/home/tom/vscode/Python/furry.gif',))
    dispro.append(tmp)  
    i-=1
    sleep(2)
i=PAGE-1
while i>=0:
    dispro[i].start()
    sleep(1.62)
    pro[i].kill()
    sleep(1.5)
    dispro[i].kill()
    i-=1
 
    
'''
m1 = mut.Process(target=show, args=(500,-5, '/home/tom/vscode/Python/furry.gif',))
m2 = mut.Process(target=show, args=(500,-5, '/home/tom/vscode/Python/furry.gif',))
m3 = mut.Process(target=show, args=(500,5, '/home/tom/vscode/Python/furry.gif',))
m4 = mut.Process(target=show, args=(500,5, '/home/tom/vscode/Python/furry.gif',))
m1.start()
m2.start()
sleep(6)

m3.start()
m4.start()
sleep(1.5)
m1.kill()
m2.kill()

sleep(6)
m3.kill()
m4.kill()
'''