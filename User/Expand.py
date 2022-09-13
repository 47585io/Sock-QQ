#All Expand is a func, They 以隐藏菜单的形式存
#You can map their output to Mess_Box
#To add your extension function just add it as a submenu of the main menu

import tkinter as tk
from tkinter.colorchooser import Chooser, askcolor
from search_enlish.Search import History_Search,main

class Extension:
    def __init__(self,) -> None:
        self.mainmenu.add_command(label="check connect", command=self.check_connect)
        self.mainmenu.add_command(label="color chooser", command=self.colorchoose)
        self.mainmenu.add_command(
            label="Search", command=self.Search)
        pass

    def check_connect(self):
        self.output(
            ("与服务器断开连接!" if self.mess.server_is_start == 0 else "连接至服务器"))
    
    def colorchoose(self):
        color=askcolor()
        self.output(color)
    
    def Search(self):
        main()
        pass