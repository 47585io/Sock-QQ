from copy import deepcopy
from re import T
import tkinter as tk
from time import perf_counter

class GraBase:
    '''A a basic configuration class'''
    LAB_Count = 3
    BUT_Count = 6
    # lab and but init count
     
    def __init__(self) -> None:
        self.func = []
        self.index = 0
        self.atfunc=None
        self.Win_Size = [[360, 450, 1600, 1000]]
        self.Color = {"bg": "#282c34", "fg": "#abb2bf","endblack":"#1e2126",'s_blue':"#61afef",
                      "entblock": "#808080", "ffg": "#3e4451", "bubu1": "#3c4049",
                      "bubu2": "#ff9a97", "alpha": "#4b5363", "setpage": "#e8e2d4",
                      "#": "#98c379", "name": "#ca463a", "mess": "#56ab9d", "orange": "#d19a66", }
        self.Font = {"zheng": "DejaVu Sans", "alpha": "Quicksand",
                     "drak": "Quicksand Medium", "small": "Z003",
                     "beutful": "DejaVu Math TeX Gyre", "frmory": "Dingbats"}
        self.Font_size = {"small": 5, "mid": 10, "big": 20}
        self.pic_size = [100, 90]
        self.filename = ""

    def init(self,):
        self.win = tk.Tk()
        self.win.config(bg=self.Color['bg'])
        self.win.update()
        self.panda=tk.PanedWindow(self.win,bg=self.Color['bg'],width=self.Win_Size[0][0],height=self.Win_Size[0][1],sashwidth=8,borderwidth=0)
        self.bgfarme = tk.Frame(self.panda)
        self.lab_list = []
        self.but_list = []
        self.message = tk.Message(self.bgfarme)
        # the index 1 is myself but,please no search
        for i in range(self.LAB_Count):
            self.lab_list.append(tk.Label(self.bgfarme))
        for i in range(self.BUT_Count):
            self.but_list.append(tk.Button(self.bgfarme))

    def init_ent(self):
        '''quick init a ent'''
        self.entfarme = tk.Frame(self.bgfarme)
        self.ent_scro = tk.Scrollbar(self.entfarme,width=8)
        #self.entvar=tk.StringVar()
        self.ent = tk.Entry(self.entfarme,)
# on, please wirte all init fun on
    def canv_init(self,):
        '''init canv and scro'''
        # self.canfarme=tk.Frame(self.bgfarme)
        self.f_can = tk.Canvas(self.bgfarme, highlightthickness=0, confine=False,
                               background=self.Color['bg'], selectbackground=self.Color['ffg'], selectforeground='white', borderwidth=0,)
        self.f_scro = tk.Scrollbar(self.bgfarme,width=8)

    def topinit(self):
        self.Win_Size.append(
            (250, 300, self.Win_Size[0][2]+self.Win_Size[0][0], self.Win_Size[0][3],))
        self.win2 = tk.Toplevel(self.win, bg=self.Color['bg'])
        self.toplist = tk.Listbox(self.win2)
        self.toplab = tk.Label(self.win2)
        self.topxbut = tk.Button(self.win2)
        self.topbut = tk.Button(self.win2)
        self.topscro = tk.Scrollbar(self.win2)

    def geostr(self,s_str,split):
        '''win str to size'''
        tup=[]
        for ch in split:
            s_lis=s_str.split(ch,1)
            tup.append(int(s_lis[0]))
            s_str=s_lis[1]
        tup.append(s_str)
        return tup
       
    def geosize(self, tup=None):
        '''win size to str'''
        if tup:
            return str(tup[0])+"x"+str(tup[1])+"+"+str(tup[2])+"+"+str(tup[3])
        return str(self.Win_Size[0][0])+"x"+str(self.Win_Size[0][1])+"+"+str(self.Win_Size[0][2])+"+"+str(self.Win_Size[0][3])

    def topclose(self,top):
        top.geometry("0x0-1000-1000")

    def clear(self):
        '''forget all lab on the bgfarme '''
        for wed in self.bgfarme.winfo_children():
            try:
                wed.pack_forget()
            except:
                try:
                    wed.grid_forget()
                except:
                    wed.place_forget()

    def go(self, go_fun, src_fun=None, mid_fun=None):
        '''use the fun go a new func, and save src fun, if you want to do other things,please give me the fun'''
        if mid_fun:
            mid_fun()
        self.but_list[4].place_forget()
        self.atfunc=go_fun
        
        self.clear()
        self.but_list[1].pack(anchor='nw')
        self.but_list[4].place(x=self.Font_size['mid']*4,y=0)
        if src_fun:
            self.index += 1
            self.func.append(src_fun)
        go_fun()

    def retu(self,mid_fun=None):
        '''pop and call a fun from func'''
        if mid_fun:
            mid_fun()
        if self.index < 1:
            exit(0)
        self.but_list[4].place_forget()
        self.clear()
        self.but_list[1].pack(anchor="nw")
        self.but_list[4].place(x=self.Font_size['mid']*4,y=0)
        #self.lab_list[3].place(x=self.Win_Size[0][0]//2-50, y=0)
        self.index -= 1
        fun = self.func[self.index]
        self.atfunc=fun
        fun()
        # print("finsh!")
        del self.func[self.index]
    
    def refresh(self,mid_fun=None):
        if mid_fun:
            mid_fun()
        #self.go(self.atfunc)
        
        self.func.append(self.atfunc)
        self.index += 1
        self.retu()

    def sleep(self,time):
        start_time=perf_counter()
        end_time=start_time+time
        while start_time<end_time:
            pass

    def winconfig(self):
        self.win.config(bg=self.Color["bg"],)
        self.win.title("Sock QQ")
        #self.win.geometry(str(self.Win_Size[0][0])+"x"+str(self.Win_Size[0][1]))
        tup=self.geostr(self.win.geometry(),("x","+","+"))
        self.Win_Size[0][2]=int(tup[2])
        self.Win_Size[0][3]=int(tup[3])
        self.win.resizable(0, 0)
        self.bgfarme.config(
            background=self.Color["bg"], width=self.Win_Size[0][0], height=self.Win_Size[0][1])
        self.panda.add(self.bgfarme)
        self.panda.pack()
        # olny set once

    def labconfig(self, lab_list):
        for lab in lab_list:
            lab.config(anchor="nw", font=(self.Font["zheng"], self.Font_size["mid"]),
                       borderwidth=0, foreground=self.Color["fg"], background=self.Color["bg"], width=int(self.Win_Size[0][0]/self.Font_size["mid"]))

    def butconfig(self, but_list):
        for but in but_list:
            but.config(font=(self.Font["zheng"], self.Font_size["mid"]),
                       borderwidth=0, highlightthickness=0, activebackground=self.Color["ffg"],  foreground=self.Color["fg"], activeforeground=self.Color["fg"], background=self.Color["bg"])

    def ent_config(self):
        self.entfarme.config(background=self.Color['bg'],)
        self.ent_scro.config(command=self.ent.xview, background=self.Color['fg'],
                             activebackground=self.Color["entblock"], borderwidth=0, orient=tk.HORIZONTAL, elementborderwidth=0, activerelief="sunken")
        self.ent.config(xscrollcommand=self.ent_scro.set, borderwidth=1, highlightbackground=self.Color['fg'],
                        highlightcolor=self.Color['fg'],
                        highlightthickness=1, insertbackground=self.Color['s_blue'],
                        bd=0, background=self.Color['bg'], fg=self.Color['fg'],)
        self.ent.pack(side='top')
        self.ent_scro.pack(side="bottom", fill=tk.X)
# please wirte all config fun on
    def canvconfig(self, canv, scro):
        '''config a Canv with Theme'''
        canv.config(width=self.Win_Size[0][0]-1, height=self.Win_Size[0]
                    [1]-1, borderwidth=0, yscrollcommand=scro.set, highlightthickness=0)
        scro.config(command=canv.yview, background=self.Color['fg'],
                    activebackground=self.Color["entblock"], borderwidth=0, elementborderwidth=0, activerelief="sunken")
        canv.configure(scrollregion=(0, 0, 500, len(
            self.furry_l)*self.pic_size[1]+500))
        canv.yview_moveto(0.0)

    def listconfig(self, list, scro):
        list.config(background=self.Color['bg'], selectbackground=self.Color['ffg'], selectmode="multiple",
                    yscrollcommand=scro.set, foreground=self.Color['fg'], selectforeground=self.Color['fg'], borderwidth=0, highlightthickness=0)
        scro.config(command=list.yview, background=self.Color['fg'],
                    activebackground=self.Color["entblock"], borderwidth=0, elementborderwidth=0, activerelief="sunken")
    
    def topconfig(self,lab,but,list,scro):
        self.win2.overrideredirect(True)
        self.win2.update()
        self.win2.attributes("-alpha", 1.0)
        
        self.butconfig(but)
        self.listconfig(list,scro)
        lab.config(text=" File Box               ", font=(self.Font["zheng"], self.Font_size["mid"]),
                   borderwidth=0, foreground=self.Color["fg"], background=self.Color["bg"],)
        lab.grid(row=0,column=0)
        but[1].config(text="×", command=lambda :self.topclose(self.win2))
        
        scro.grid(row=1,column=1)
        list.grid(row=1,column=0,rowspan=1)
        but[1].grid(row=0, column=1)
        but[0].grid(row=2,column=1)
        
    def quickconfig(self, mess, sock):
        '''usally, user olny call it, can init and config all lab'''
        self.sock = sock
        self.mess = mess
        self.init()
        self.winconfig()
        self.labconfig(self.lab_list)
        self.butconfig(self.but_list)
        self.init_ent()
        self.ent_config()
        self.but_list[1].config(text="←", command=lambda: self.retu())
        self.but_list[4].config(text="↻", command=lambda: self.refresh())
