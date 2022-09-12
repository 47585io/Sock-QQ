import tkinter as tk
from time import perf_counter
import threading as th
from User.Base import GraBase
from time import sleep

class Mess_Box(GraBase):
    def __init__(self) -> None:
        self.after_time=0
        self.before_time=0
        self.messth=th.Thread(target=self.timing)
        self.messth.setDaemon(True)
        self.atstr=[]
        self.strvar=tk.StringVar()
        self.mess_y=0
        self.messth.start()
        
    def init(self,win):
        self.win=win
        self.messtop=tk.Toplevel(win)
        self.messxbut = tk.Button(
            self.messtop, command=lambda: self.topclose(self.messtop),text="x")
        self.messlab=tk.Label(self.messtop,textvariable=self.strvar)
        self.messxbut.pack(anchor='ne',side='right',)
        self.messlab.pack()
        self.topclose(self.messtop)
       
    def messshow(self,):
        pos_str=self.win.geometry()
        pos=self.geostr(pos_str,('x','+','+'))
        pos_str=self.geosize((200,100,int(pos[2])+500,int(pos[3])+100))
        self.messtop.geometry(pos_str)
    
    def start(self,time):
        '''start show, set a time'''
        self.before_time=perf_counter()
        if time:
            self.after_time=self.before_time+time
        else:
            self.after_time = self.before_time+20
    
    def timing(self):
        sleep(5)
        while 1:
            while self.before_time < self.after_time:
                if self.strvar.get()!=self.atstr[0]:
                    self.start(None)
                    self.strvar.set(self.atstr[0])
                    self.messshow() 
                self.before_time = perf_counter()        
            self.topclose(self.messtop)
        
    
    
    