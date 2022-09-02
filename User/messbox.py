import tkinter as tk
from urllib.parse import ParseResult, ParseResultBytes


class messbox:
    def __init__(self) -> None:
        self.win=tk.Tk()
        self.list=tk.Listbox(self.win)
        self.mess=tk.Message(self.win)
        self.lab=tk.Label(self.win)
        
    def show(self,title,s_str,yes="no",isx=1):
#window title, show s_str, yes or no use list(when now, s_str is a list),isx:yes or no the window has X
        pass
    
    def resize(w,h):
        pass
    
    def move(x,y):
        pass
    
    def toto(self):
#window start show pop
        pass
    