from User.Talk_with import Talk_with,tk

class Seting(Talk_with):
    def __init__(self) -> None:
        super().__init__()
        self.pan_y=0
        self.pan_tag=[]
    def init(self):
        super().init()
        self.panframe=tk.Frame(self.panda)
        self.pancanv=tk.Canvas(self.panframe)
    def showfriends(self):
        super().showfriends()
        self.but_list[0].place(x=self.Win_Size[0][0]-70, y=0)
        self.but_list[5].config(text="◎",command=self.Seting)
        self.but_list[5].place(x=self.Win_Size[0][0]-35, y=0)
    def Seting(self):
        self.panda.forget(self.bgfarme)
        self.panda.add(self.panframe)
        self.panda.add(self.bgfarme)
        self.pancanv.create_text
        pass