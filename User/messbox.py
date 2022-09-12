import tkinter as tk
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor as T

class Mess_Box:
    def __init__(self) -> None:
        self.after_time=0
        self.before_time=0
        self.messth=T(1) 
        self.atstr=[]
        self.strvar=tk.StringVar()
        self.mess_y=0
        
    def messinit(self,win):
        self.messtop=tk.Toplevel(win)
        self.messxbut = tk.Button(
            self.messtop, command=lambda: self.topclose(self.messtop),text="x")
        self.messlab=tk.Message(self.messtop,textvariable=self.strvar)
        self.messxbut.pack(anchor='ne',side='right',)
        self.messlab.pack()
        self.messtop.overrideredirect(True)
        #self.messtop.update()
        self.messtop.attributes("-alpha", 1.0)
        self.topclose(self.messtop)
       
    def messshow(self,):
        '''open show window'''
        pos_str=self.win.geometry()
        pos=self.geostr(pos_str,('x','+','+'))
        pos_str=self.geosize((250,300,int(pos[2])+500,int(pos[3])+100))
        self.messtop.geometry(pos_str)
    
    def starttime(self,time):
        '''start show, set a time'''
        self.before_time=perf_counter()
        if time:
            self.after_time=self.before_time+time
        else:
            self.after_time = self.before_time+20
    
    def reset(self,s):
        ''''''
        self.atstr.append(s)
    
    def to(self):
        '''start timing'''
        self.messth.submit(self.timing)
    
    def timing(self):
        '''None'''
        while self.before_time < self.after_time:
            if self.strvar.get()!=str(self.atstr[0]):
                self.starttime(None)
                self.strvar.set(str(self.atstr[0])) 
            self.before_time = perf_counter() 
            self.messshow()
            self.messtop.update()       
        self.topclose(self.messtop)
        
    
    
    