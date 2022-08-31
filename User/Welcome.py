from time import sleep
import tkinter.filedialog as fid
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import greenlet
import threading as th
import os
USER_NAME = ""
MAX_THD = 1
# the user can use every work max thread


class Welcome:
    '''the welcom class, can show welcome page and switch page'''
    LAB_Count = 3
    BUT_Count = 3
    # lab and but init count

    def __init__(self) -> None:
        self.func = []
        self.index = 0
        self.Win_Size = [(360, 450, 1600, 1000)]
        self.Color = {"bg": "#282c34", "fg": "#abb2bf",
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
            return str(tup[0][0])+"x"+str(tup[0][1])+"+"+str(tup[0][2])+"+"+str(tup[0][3])
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

    def retu(self,):
        '''pop and call a fun from func'''
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
        #self.win.resizable(0, 0)
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

    def run(self):
        '''when config all lab , call it'''
        global USER_NAME
        tmp = self.openfile()
        if self.openfile() == 0:
            self.go(self.welcome1)
        else:
            USER_NAME = tmp[0][0:-1:]
            self.filename = tmp[1]
            self.go(self.Login)
        self.win.mainloop()
        self.new()
        self.win.mainloop()

    def welcome1(self):
        self.lab_list[0].config(text="\nWelcome!", font=(
            self.Font["zheng"], 20, "bold"))
        self.lab_list[0].pack()
        self.lab_list[1].config(text="\n\n一切刚刚好,现在立刻!\n\n",)
        self.lab_list[1].pack()
        self.but_list[0].config(
            text="Get Started", command=lambda: self.go(self.welcome2, self.welcome1))
        self.but_list[0].pack(side='right')
        # print("call!")

    def welcome2(self):
        # print("&")
        self.lab_list[0].config(text='\nSet Name',)
        self.lab_list[0].pack()
        self.lab_list[1].config(text="\n伟大的名字\n ")
        self.lab_list[1].pack()
        self.entfarme.pack()
        self.lab_list[2].config(text="\n")
        self.lab_list[2].pack()
        self.but_list[0].config(text="Enter", command=lambda: self.go(
            self.welcome3, self.welcome2, self.setname))
        self.but_list[0].pack(side='right')
        self.ent.bind("<Return>", lambda k, x=self.welcome3,
                      y=self.welcome2, z=self.setname: self.go(x, y, z))

    def welcome3(self):
        self.ent.unbind("<Return>")
        self.lab_list[0].config(text="\nChoose Avatar\n")
        self.lab_list[0].pack()
        self.lab_list[1].config(text="漂亮的头像\n")
        self.lab_list[1].pack()
        self.message.config(anchor="nw", font=(self.Font["zheng"], self.Font_size["mid"]),
                            foreground=self.Color["fg"], background=self.Color["bg"], width=self.Win_Size[0][0]-20)
        self.message.pack()
        self.but_list[0].config(command=self.choose,
                                text='Choose', borderwidth=0,)
        self.but_list[0].pack(side='left',)
        self.but_list[2].config(command=lambda: self.go(
            self.Login, self.welcome3, self.save), text="Login")
        self.but_list[2].pack(side='right')
    # on, three welcome page is really, after, you must set a login func

    def choose(self,):
        '''open file chooser'''
        self.filename = fid.askopenfilename(
            initialdir="../", filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("GIF", "*.gif"), ])
        if self.filename != ():
            self.message.config(text=self.filename+"\n")

    def save(self):
        '''save user choose picture'''
        if self.filename == ():
            return
        if self.filename.find(".jpg"):
            newfile = Image.open(self.filename, "r")
            newfile.thumbnail((300, 700))
            newfile.convert("RGBA")
            mk = os.path.abspath("./")
            newfile.save(mk+"/new.png")
            self.filename = mk+"/new.png"
            print("save in ", mk+"/new.png")
        file = open("name.txt", "w")
        file.writelines([USER_NAME+"\n", self.filename])
        file.close()

    def setname(self):
        global USER_NAME
        USER_NAME = self.ent.get()
        print("hello", USER_NAME)

    def openfile(self):
        '''check a can use file'''
        file = open("name.txt", "r+")
        tmp = file.readlines()
        if tmp == []:
            return 0
        else:
            return tmp

    def Login(self):
        '''after login, going to show friends'''
        global USER_NAME
        self.lab_list[0].config(text='\nHello!\n', anchor='center', font=(
            self.Font["zheng"], self.Font_size["big"], "bold"))
        self.lab_list[0].pack()
        self.message.config(text=USER_NAME, anchor="nw", font=(self.Font["zheng"], self.Font_size["mid"]),
                            foreground=self.Color["fg"], background=self.Color["bg"], width=self.Win_Size[0][0]-20)

        self.furry = tk.PhotoImage(file=self.filename)
        self.lab_list[1].config(width=self.pic_size[0],
                                height=self.pic_size[1], image=self.furry)
        self.lab_list[1].pack()
        self.lab_list[2].pack()
        self.message.pack()
        self.win.update()
        self.mess.Send(self.sock, "LOGIN "+USER_NAME)
        for i in range(MAX_THD):
            r = th.Thread(target=self.mess.Read, args=(self.sock,))
            r.setDaemon(True)
            r.start()
        sleep(2)
        self.cache1.switch()
        # jump to show

    def new(self):
        '''this is Extended access'''
        pass
