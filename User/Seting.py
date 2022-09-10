from User.Talk_with import Talk_with,tk
from tkinter import colorchooser
from time import sleep
from Pubilc.Split import Spilt_Mess

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
        self.panframe = tk.PanedWindow(self.panda, orient="vertical",sashwidth=6,bg=self.Color['s_blue'] 
                                       ,borderwidth=0,)
        self.pancanv = tk.Canvas(self.panframe, bg=self.Color['setpage'])
        self.panframe.add(self.pancanv)
        self.panson=tk.Frame(self.panframe,)
        self.text_init()
        
#panda has two member: panframe and  bgfarme, bgfarme is front page, so add it in init
#when user click the Seting Button, show the Setting page, so now add panframe in self.Setting
#the panframe have two member: pancanv and panson, pancanv show fllow panframe, so can show first, and becuse pancanv on panframe, so olny show panframe, just show pancanv
#when uset click the pancanv obj, show the pantext, so add panson to panframe in after
    
    def Closeall(self):
        '''when user close the window, saveall and exit'''
        self.isstart=0
        sleep(0.5)
        self.history.saveall(self.fren)
        #self.savetext()
        exit(0)
    
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
        def get_line(s):
            tup=[]
            index=0
            while index!=-1:
                tmp=index
                if index==0:
                    tmp=-1
                index=s.find('\n',index+1)
                tup.append(s[tmp+1:index+1:])  
            return tup
        
        def get_index(line,row,index):
            relis=[]
            lis=Spilt_Mess.Friend_list_Read_Spilt(line.encode())
            for l in lis:
                index=line.find(l,index)
                relis.append((str(row)+"."+str(index), str(row)+"."+str(index+len(l))))
            return relis
        
        tup=get_line(s)     
        text.insert("end",s)
        
        name_list=[]
        list_=[]
        mess_list=[]  
        i=1
        for s in tup:
            index=s.find("###")
            if index:
                name_list.append((str(i)+"."+str(0),str(i)+"."+str(index)))
                list_.append((str(i)+"."+str(index), str(i)+"."+str(index+3)))
                index+=3
                mess_list.append(get_index(s,i,index))
            i+=1
        for name in name_list:
            text.tag_add("name",name[0],name[1])
        for a in list_:
            text.tag_add("#",a[0],a[1])
        for mess in mess_list:
            for m in mess:
                text.tag_add("mess",m[0],m[1])
        text.tag_config("name",foreground='red')  
        text.tag_config("#",foreground='green')  
        text.tag_config("mess",foreground='blue')  
    
    def savetext(self,):
        if self.textlab['text']:
            file=open(self.textlab['text'],"w")
            file.write(self.pantext.get("0.0","end"))
            file.close()
    
    def opentext(self,event):
       # self.savetext()
        tup = self.pancanv.find_closest(event.x, event.y)
        index = self.pan_tag.index(tup[0])
        name=self.setstr4[index]
        self.textlab.config(text=name)
        
        file=open(name,"r")
        s=file.read()
        file.close()
        self.pantext.delete("0.0","end")
        self.panframe.add(self.panson)
        self.color_insert(self.pantext,s)
       
