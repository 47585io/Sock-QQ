import tkinter as tk
from time import sleep

class messbox:
    def __init__(self) -> None:
        self.win=tk.Tk()
        self.bgframe=tk.Frame(self.win)
        self.list=tk.Listbox(self.bgframe)
        self.mess=tk.Message(self.bgframe)
        self.lab=tk.Label(self.bgframe)
        self.but=tk.Button(self.bgframe)
        self.okbut=tk.Button(self.bgframe)
        self.scro=tk.Scrollbar(self.bgframe)
        self.init()
        self.quickconfig()
    def init(self):
        self.Win_Size = [[100, 200, 1600, 1000]]
        self.Color = {"bg": "#282c34", "fg": "#abb2bf", "endblack": "#1e2024",
              "entblock": "#808080", "ffg": "#3e4451", "bubu1": "#3c4049",}
        self.Font = {"zheng": "DejaVu Sans", "alpha": "Quicksand",
                           "drak": "Quicksand Medium", "small": "Z003",
                           "beutful": "DejaVu Math TeX Gyre", "frmory": "Dingbats"}
        self.Font_size = {"small": 5, "mid": 10, "big": 20}
        
    def quickconfig(self):
        self.win.overrideredirect(True)
        self.win.config(bg=self.Color['bg'])
        self.bgframe.config(bg=self.Color['bg'])
    
    def geosize(self, tup=None):
        '''win size to str'''
        if tup:
            return str(tup[0])+"x"+str(tup[1])+"+"+str(tup[2])+"+"+str(tup[3])
        return str(self.Win_Size[0][0])+"x"+str(self.Win_Size[0][1])+"+"+str(self.Win_Size[0][2])+"+"+str(self.Win_Size[0][3])
       
    def show(self, title, s_str,  pos, yes="no",srcpos=(), count=20, isx=1):
#window title, show s_str,window pos, yes or no use list(when now, s_str is a list),isx:yes or no the window has X
        if isx == 1:
            self.but.config(text="x", command=self.win.quit)
            self.but.pack(side='right')
    
    def resize(self,w,h):
        self.win.geometry(self.geosize((w,h,self.Win_Size[0][2],self.Win_Size[0][3])))
    
    def move(self,x,y):
        self.win.geometry(self.geosize(
            (self.Win_Size[0][0], self.Win_Size[0][1],x,y)))
    
    def toto(self,tox,toy,thecount=20):
#window start show pop
        divx=self.Win_Size[0][2]-tox
        divy=self.Win_Size[0][3]-toy
        for i in range(thecount):
            self.move(self.Win_Size[0][2]- divx//thecount, self.Win_Size[0][3]- divy//thecount)
            self.win.update()
            sleep(0.05)