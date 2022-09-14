#All Expand is a func, They 以隐藏菜单的形式存
#You can map their output to Mess_Box
#To add your extension function just add it as a submenu of the main menu

import tkinter as tk
from tkinter.colorchooser import Chooser, askcolor
from User.Search import main
from tkinter.font import families

class Extension:
    def __init__(self,) -> None:
        self.isopen=0
        self.mainmenu.add_command(label="check connect", command=self.check_connect)
        self.mainmenu.add_command(label="color chooser", command=self.colorchoose)
        self.mainmenu.add_command(label="font chooser",command=self.fontchoose)
        self.mainmenu.add_command(label="Search", command=self.Search)

    def check_connect(self):
        self.output(
            ("与服务器断开连接!" if self.mess.server_is_start == 0 else "连接至服务器"))
    
    def other_clear(self):
        for wed in self.messtop.winfo_children():
            wed.pack_forget()
        self.isopen=0
    
    def colorchoose(self):
        color=askcolor()
        self.output(color)
    
    def fontchoose(self):
        self.panframe.add(self.panson)
        self.output("字体已经在 设置>Edit 打开")
        self.textlab.config(text="字体")
        tup=families()
        self.pantext.delete("0.0","end")
        i=0
        for t in tup:
            self.pantext.insert("end",t+"\n")
            self.pantext.tag_add(str(i),str(i)+".0",str(i)+"."+str(len(t)))
            self.pantext.tag_configure(str(i),font=(t,))
            i+=1
    
    def Search(self):
        self.messshow()
        if self.isopen==0:
            self.isopen=1
            main(self)
    