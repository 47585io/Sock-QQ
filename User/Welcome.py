from time import sleep
import tkinter.filedialog as fid
from tkinter import messagebox
from PIL import Image
import os
import greenlet
import abc

from User.Base import GraBase, tk
USER_NAME = ""


class Welcome(GraBase):
    '''the welcom class, can show welcome page'''

    def __init__(self) -> None:
        super().__init__()
        self.User_Name = USER_NAME
        self.cache1 = greenlet.greenlet(self.new)
        
    def run(self):
        '''when config all lab , call it'''
        tmp = self.openfile()
        if self.openfile() == 0:
            self.go(self.welcome1)
        else:
            self.User_Name = tmp[0][0:-1:]
            self.filename = tmp[1]
            self.go(self.Login)
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
        file.writelines([self.User_Name+"\n", self.filename])
        file.close()

    def setname(self):
        self.User_Name = self.ent.get()
        print("hello", self.User_Name)

    def openfile(self):
        '''check a can use file'''
        if not os.path.isfile("./name.txt"):
            return 0
        file = open("name.txt", "r")
        tmp = file.read()
        if not tmp:
            return 0
        else:
            index=tmp.find("###")
            i=len(tmp)-1
            while tmp[i]=='\n':
                i-=1
            return (tmp[0:index+1:],tmp[index+3:i+1:])

    def Login(self):
        '''after login, going to show friends'''
        self.lab_list[0].config(text='\nHello!\n', anchor='center', font=(
            self.Font["zheng"], self.Font_size["big"], "bold"))
        self.lab_list[0].pack()
        self.message.config(text=self.User_Name, anchor="nw", font=(self.Font["zheng"], self.Font_size["mid"]),
                            foreground=self.Color["fg"], background=self.Color["bg"], width=self.Win_Size[0][0]-20)

        self.furry = tk.PhotoImage(file=self.filename)
        self.lab_list[1].config(width=self.pic_size[0],
                                height=self.pic_size[1], image=self.furry)
        self.lab_list[1].pack()
        self.lab_list[2].pack()
        self.message.pack()
        self.win.update()
        sleep(0.5)
        self.cache1.switch()
        # jump to show

    def new(self):
        '''this is Extended access'''
        pass
