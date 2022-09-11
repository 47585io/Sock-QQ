import tkinter as tk
from User.Seting import Seting
from time import perf_counter

class Mess_Box(Seting):
    def __init__(self) -> None:
        super().__init__()
        self.after_time=0
        self.before_time=0
        atstr=""
    def init(self):
        super().init()
        self.messtop=tk.Toplevel(self.win)
        self.messxbut=tk.Button(self.messtop)
        self.messlab=tk.Label(self.messtop)
        self.messxbut.pack(anchor='ne',side='right')
        self.messlab.pack(side='bottom')
    def quickconfig(self, friends, mess, sock, tcpmess, tcpsock):
        super().quickconfig(friends, mess, sock, tcpmess, tcpsock)
        
    def messshow(self,):
        pos_str=self.win.geometry()
        pos=self.geostr()
        pos_str=self.geosize(pos)
        self.messtop.geometry()
    
    def start(self,time):
        '''start show, set a time'''
        self.before_time=perf_counter()
        self.after_time=self.before_time+time
        self.messshow()
    
    def reset(self,str):
        '''reset str'''
        self.messlab.config(text=str)
        self.before_time=perf_counter()
        if self.before_time > self.after_time:
            self.topclose(self.messtop)
    
    
    
    