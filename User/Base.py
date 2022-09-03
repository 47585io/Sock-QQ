import greenlet
import tkinter as tk


class GraBase:
    '''A a basic configuration class'''
    LAB_Count = 3
    BUT_Count = 4
    # lab and but init count

    def __init__(self) -> None:
        self.func = []
        self.index = 0
        self.Win_Size = [[360, 450, 1600, 1000]]
        self.Color = {"bg": "#282c34", "fg": "#abb2bf","endblack":"#1e2024",
                      "entblock": "#808080", "ffg": "#3e4451", "bubu1": "#3c4049", "bubu2": "#ff9a97", "alpha": "#4b5363"}
        self.Font = {"zheng": "DejaVu Sans", "alpha": "Quicksand",
                     "drak": "Quicksand Medium", "small": "Z003",
                     "beutful": "DejaVu Math TeX Gyre", "frmory": "Dingbats"}
        self.Font_size = {"small": 5, "mid": 10, "big": 20}
        self.pic_size = [100, 90]
        self.filename = ""
        self.cache1 = greenlet.greenlet(self.new)

    def init(self,):
        self.win = tk.Tk()
        self.bgfarme = tk.Frame(self.win)
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
        self.ent_scro = tk.Scrollbar(self.entfarme)
        self.ent = tk.Entry(self.entfarme,)
# on, please wirte all init fun on

    def geosize(self, tup=None):
        '''win size to str'''
        if tup:
            return str(tup[0])+"x"+str(tup[1])+"+"+str(tup[2])+"+"+str(tup[3])
        return str(self.Win_Size[0][0])+"x"+str(self.Win_Size[0][1])+"+"+str(self.Win_Size[0][2])+"+"+str(self.Win_Size[0][3])

    def clear(self):
        '''forget all lab on the bgfarme '''
        for wed in self.bgfarme.winfo_children():
            wed.pack_forget()

    def go(self, go_fun, src_fun=None, mid_fun=None):
        '''use the fun go a new func, and save src fun, if you want to do other things,please give me the fun'''
        if mid_fun:
            mid_fun()
        self.clear()
        self.but_list[1].pack(anchor="nw")
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
        self.clear()
        self.but_list[1].pack(anchor="nw")
        self.index -= 1
        fun = self.func[self.index]
        fun()
        # print("finsh!")
        del self.func[self.index]

    def winconfig(self):
        self.win.config(bg=self.Color["bg"],)
        self.win.title("Sock QQ")
        self.win.geometry(self.geosize())
        self.win.resizable(0, 0)
        self.bgfarme.config(
            background=self.Color["bg"], width=self.Win_Size[0][0], height=self.Win_Size[0][1])
        self.bgfarme.pack()
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
                        highlightthickness=1, insertbackground='#61afef',
                        bd=0, background=self.Color['bg'], fg=self.Color['fg'],)
        self.ent.pack(side='top')
        self.ent_scro.pack(side="bottom", fill=tk.X)
# please wirte all config fun on

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
