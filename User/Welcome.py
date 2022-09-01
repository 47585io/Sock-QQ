from time import sleep
import tkinter.filedialog as fid
from tkinter import messagebox
from PIL import Image
import os
MAX_THD = 1
# the user can use every work max thread
from User.Base import GraBase,USER_NAME,th,tk

class Welcome(GraBase):
    '''the welcom class, can show welcome page and switch page'''
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
        sleep(1.5)
        self.cache1.switch()
        # jump to show

    def new(self):
        '''this is Extended access'''
        pass
