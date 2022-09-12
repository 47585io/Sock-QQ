#All Expand is a func, They 以隐藏菜单的形式存
#You can map their output to Mess_Box
#To add your extension function just add it as a submenu of the main menu

import tkinter as tk

class Extension:
    def __init__(self,) -> None:
        self.mainmenu.add_command(label="check connect", command=self.check_connect)
        pass

    def check_connect(self):
        self.output(
            ("与服务器断开连接!" if self.mess.server_is_start == 0 else "连接至服务器"))
    