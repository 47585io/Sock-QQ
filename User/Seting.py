from User.Talk_with import Talk_with,tk
from tkinter import colorchooser

class Seting(Talk_with):
    def __init__(self) -> None:
        super().__init__()
        self.pan_y=50
        self.pan_tag=[]
        self.setstr=["要设置Sock-QQ的各项配置,请按如下格式:\n\n", 
                     "Name###['mess1','mess2'...]\n",
                     "_____________________________________\n",]
        
        self.setstr2= ["name.txt", 
                       "friend",  
                       "mess",    
                       "get",     
                       "var",     
                       "./mydir", 
                       "supurconfig"]
        self.setstr3 = ["    User's Name and pic file    ",
                        "User's Friends name and pic file",
                        "User talk mess with Friends file",
                        "User's Get str to get file file",
                        "If start, the output not display",
                        "save get file, fromwho/filename",
                        "      The End config file      "]
        self.setstr4=["./name.txt",
                      "./mydir/friend",
                      "./mydir/mess",
                      "./mydir/get",
                      "./mydir/var",
                      "./mydir",
                      "./mydir/supurconfig"]
    
    def text_init(self):
        self.pantext = tk.Text(self.panson, borderwidth=0, highlightthickness=0,
                                width=self.Win_Size[0][0], height=self.Win_Size[0][1], bg=self.Color['setpage'])
        self.textlab=tk.Label(self.panson)
        self.textlab.pack()
        self.text_scro=tk.Scrollbar(self.panson,)
        self.pantext.config(yscrollcommand=self.text_scro.set)
        self.text_scro.config(command=self.pantext.yview, background=self.Color['fg'],
                              activebackground=self.Color["entblock"], borderwidth=0, elementborderwidth=0, activerelief="sunken")
        self.text_scro.pack(side='right',fill=tk.Y,)
        self.pantext.pack()
     
    def init(self):
        super().init()
        self.panframe = tk.PanedWindow(self.panda, orient="vertical",sashwidth=6)
        self.pancanv = tk.Canvas(self.panframe, bg=self.Color['setpage'])
        self.panframe.add(self.pancanv)
        self.panson=tk.Frame(self.panframe,)
        self.text_init()
        
#panda has two member: panframe and  bgfarme, bgfarme is front page, so add it in init
#when user click the Seting Button, show the Setting page, so now add panframe in self.Setting
#the panframe have two member: pancanv and panson, pancanv show fllow panframe, so can show first, and becuse pancanv on panframe, so olny show panframe, just show pancanv
#when uset click the pancanv obj, show the pantext, so add panson to panframe in after
    
    def textconfug():
        pass
    
    def new(self):
        super().new()
        for s in self.setstr:
            self.draw_a_text(
                self.pancanv, s, (self.Win_Size[0][0]//2-20, self.pan_y))
            self.pan_y += 30

        i = 0
        while i < len(self.setstr2):
            self.draw_a_text(
                self.pancanv, self.setstr2[i], (self.Win_Size[0][0]//6, self.pan_y), "red", self.opentext)
            self.draw_a_text(
                self.pancanv, self.setstr3[i], (self.Win_Size[0][0]//2+self.Win_Size[0][0]//6//2, self.pan_y),)
            self.pan_y += 50
            i += 1
        self.pan_y += 100
        self.pancanv.create_text(self.Win_Size[0][0]/2,self.pan_y,text="选中上面的文件后,将下面的分割条往上拉↓")
    
    def showfriends(self):
        super().showfriends()
        self.pancanv.config(
            width=self.Win_Size[0][0], height=self.Win_Size[0][1])
        self.but_list[0].place(x=self.Win_Size[0][0]-70, y=0)
        self.but_list[5].config(text="◎",command=self.Seting)
        self.but_list[5].place(x=self.Win_Size[0][0]-35, y=0)
       
    def draw_a_text(self,canv,s,pos,color="#000000",fun=None):
        tag=canv.create_text(pos[0],pos[1],text=s,fill=color,activefill="black")
        if fun:
            self.pan_tag.append(tag)
            canv.tag_bind(tag,"<Button-1>",fun)
    
    def Seting(self):
        #self.panda.forget(self.bgfarme)
        self.panda.add(self.panframe,)
        #self.panda.add(self.bgfarme)
        #self.win.bell()
    
    def color_insert(self,text,s):
        pass
    
    def opentext(self,event):
        tup = self.pancanv.find_closest(event.x, event.y)
        index = self.pan_tag.index(tup[0])
        name=self.setstr4[index]
        self.textlab.config(text=name)
        file=open(name,"r")
        s=file.read()
        self.pantext.delete("0.0","end")
        self.panframe.add(self.panson)
        self.color_insert(self.pantext,s)
        file.close()
