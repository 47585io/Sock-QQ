import tkinter as tk
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor as T

class Mess_Box:
    def __init__(self) -> None:
        self.after_time=0
        self.before_time=0
        self.messth=T(1) 
        self.atstrlist=[]
        self.atstr=""
        self.strvar=tk.StringVar()
        self.mess_y=0
        self.mess_start=0
        
    def messinit(self,win):
        self.messtop=tk.Toplevel(win)
        self.messxbut = tk.Button(
            self.messtop, command=lambda: self.topclose(self.messtop),text="×",borderwidth=0,highlightthickness=0)
        self.messlab=tk.Message(self.messtop,textvariable=self.strvar,width=200)
        self.messxbut.pack(anchor='ne',side='right',)
        self.messlab.pack()
        self.messtop.overrideredirect(True)
        #self.messtop.update()
        self.messtop.attributes("-alpha", 1.0)
        self.topclose(self.messtop)
     
    def output(self,s_str):
     self.starttime(20)
     self.atstrlist.append(s_str)
     if self.mess_start==0:
        self.to()
         
    def messshow(self,):
        '''open show window'''
        pos_str=self.win.geometry()
        pos=self.geostr(pos_str,('x','+','+'))
        pos_str=self.geosize((250,300,int(pos[2])+int(pos[0]),int(pos[3])+self.Win_Size[1][1]))
        self.messtop.geometry(pos_str)
    
    def starttime(self,time):
        '''start show, set a time'''
        self.before_time=perf_counter()
        if time:
            self.after_time=self.before_time+time
        else:
            self.after_time = self.before_time+20
    
    def to(self):
        '''start timing'''
        self.mess_start = 1
        self.messth.submit(self.timing)
    
    def castr(self):
        self.atstr=""
        for a in self.atstrlist:
            self.atstr+=str(a)+"\n"
    
    def timing(self):
        '''None'''
        while self.before_time < self.after_time:
            self.castr()
            if self.mess_start == 0:
                print("mess return")
                return
            if self.strvar.get()!=self.atstr:          
                self.starttime(None)
                self.strvar.set(self.atstr) 
                self.messshow()
            self.before_time = perf_counter() 
            self.messtop.update()  
        self.atstrlist.clear()     
        self.topclose(self.messtop)
        self.mess_start=0
        
    
    
    