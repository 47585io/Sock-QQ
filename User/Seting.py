from User.Talk_with import Talk_with,tk

class Seting(Talk_with):
    def __init__(self) -> None:
        super().__init__()
        self.pan_y=50
        self.pan_tag=[]
        self.setstr=["要设置Sock-QQ的各项配置,请按如下格式:\n\n", "Name###['mess1','mess2'...]\n",
                     "_____________________________________\n","name.txt      User's Name and pic file"]
    def init(self):
        super().init()
        self.panframe=tk.Frame(self.panda)
        self.pancanv=tk.Canvas(self.panframe,width=self.Win_Size[0][0])
        self.pancanv.pack()
    def showfriends(self):
        super().showfriends()
        self.pancanv.config(width=self.Win_Size[0][0])
        self.but_list[0].place(x=self.Win_Size[0][0]-70, y=0)
        self.but_list[5].config(text="◎",command=self.Seting)
        self.but_list[5].place(x=self.Win_Size[0][0]-35, y=0)
    def draw_a_text(self,canv,s,pos,color,fun):
        canv.create_text(pos[0],pos[1],text=s,)
        pass
    def Seting(self):
        #self.panda.forget(self.bgfarme)
        self.panda.add(self.panframe,)
        #self.panda.add(self.bgfarme)
        #self.win.bell()

        for s in self.setstr:
            self.draw_a_text(self.pancanv,s,(self.Win_Size[0][0]//2-20,self.pan_y),0,0)
            self.pan_y+=30
