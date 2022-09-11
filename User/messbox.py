import tkinter as tk
from User.Seting import Seting
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor as Th

class Mess_Box(Seting):
    def __init__(self) -> None:
        super().__init__()
        self.after_time=0
        self.before_time=0
        self.messth=Th(1)
        self.mess_list=()
    def init(self):
        super().init()
        self.messtop=tk.Toplevel(self.win)
        self.messxbut=tk.Button(self.messtop)
        self.messlab=tk.Label(self.messtop)
        self.messxbut.pack(anchor='ne',side='right')
        self.messlab.pack(side='bottom')
    def quickconfig(self, friends, mess, sock, tcpmess, tcpsock):
        super().quickconfig(friends, mess, sock, tcpmess, tcpsock)
        self.topclose(self.messtop)
        
    def messshow(self,):
        pos_str=self.win.geometry()
        pos=self.geostr()
        pos_str=self.geosize((200,100,pos[2]+300,pos[3]+500))
        self.messtop.geometry()
    
    def start(self,time):
        '''start show, set a time'''
        self.before_time=perf_counter()
        self.after_time=self.before_time+time
        self.messshow()
        self.messth.submit(self.reset)
    
    def reset(self,):
        '''reset str'''
        while self.before_time > self.after_time:
            self.messlab.config(text=str)
            self.before_time=perf_counter()
            self.messtop.update()
        self.topclose(self.messtop)
    
    
    
    
    