
from User.Talk_with import Talk_with,tk
from tkinter import filedialog as f
from time import sleep
from Pubilc.Split import Spilt_Mess
import os
from User.Expand import Extension

class Seting(Talk_with,Extension):
    def __init__(self) -> None:
        super().__init__()
        self.pan_y=50
        self.pan_tag=[]
        self.atpic=None
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
    
    def popmenu(self,event):
        self.mainmenu.post(event.x_root, event.y_root)
    def unpop(self,event):
        self.mainmenu.unpost()
    
    def text_init(self):
        self.pantext = tk.Text(self.panson, borderwidth=0, highlightthickness=0,undo=True,insertbackground=self.Color['s_blue'],
                                width=self.Win_Size[0][0], height=self.Win_Size[0][1], bg=self.Color['setpage'],insertwidth=3)
        self.textlab=tk.Label(self.panson)
        self.textlab.pack()
        self.text_scro=tk.Scrollbar(self.panson,width=6)
        self.pantext.config(yscrollcommand=self.text_scro.set)
        self.text_scro.config(command=self.pantext.yview, background=self.Color['fg'],
                              activebackground=self.Color["entblock"], borderwidth=0, elementborderwidth=0, activerelief="sunken")
        self.text_scro.pack(side='right',fill=tk.Y,)
        self.pantext.pack()
     
    def init(self):
        super().init()
        self.panframe = tk.PanedWindow(self.panda, orient="vertical",sashwidth=10,bg=self.Color['setpage'] 
                                       ,borderwidth=0,)
        self.pancanv = tk.Canvas(
            self.panframe, bg=self.Color['setpage'], borderwidth=0, highlightthickness=0,)
        self.panframe.add(self.pancanv)
        self.panson=tk.Frame(self.panframe,)
        self.text_init()
        self.mainmenu = tk.Menu(self.win, tearoff=False,activebackground=self.Color['s_blue'], borderwidth=0,)
        Extension.__init__(self)
        self.win.bind("<Button-3>",self.popmenu)
        self.win.bind("<Button-1>",self.unpop)
        
#panda has two member: panframe and  bgfarme, bgfarme is front page, so add it in init
#when user click the Seting Button, show the Setting page, so now add panframe in self.Setting
#the panframe have two member: pancanv and panson, pancanv show fllow panframe, so can show first, and becuse pancanv on panframe, so olny show panframe, just show pancanv
#when uset click the pancanv obj, show the pantext, so add panson to panframe in after


    def Closeall(self):
        '''when user close the window, saveall and exit'''
        self.tcpmess.isget = 0
        self.tcpmess.issend=0
        self.isstart=0
        self.mess_start = 0
        sleep(0.5)
        self.history.saveall(self.fren)
        self.savetext()
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
                self.pancanv, self.setstr2[i], (self.Win_Size[0][0]//6, self.pan_y), self.Color['name'], self.check_file)
            self.draw_a_text(
                self.pancanv, self.setstr3[i], (self.Win_Size[0][0]//2+self.Win_Size[0][0]//6//2, self.pan_y),)
            self.pan_y += 50
            i += 1
            
        self.pan_y += 100
        self.pancanv.create_text(self.Win_Size[0][0]/2,self.pan_y,text="选中 or 打开文件后,将下面的分割条往上拉↓")
    
    def showfriends(self):
        super().showfriends()
        self.pancanv.config(
            width=self.Win_Size[0][0], height=self.Win_Size[0][1])
        self.but_list[0].place(x=self.Win_Size[0][0]-70, y=0)
        self.but_list[5].config(text="◎",command=self.Seting)
        self.but_list[5].place(x=self.Win_Size[0][0]-35, y=0)
       
    def draw_a_text(self,canv,s,pos,color="#000000",fun=None):
        tag=canv.create_text(pos[0],pos[1],text=s,fill=color,activefill='black')
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
            
        text.insert("end",s)
        tup = get_line(s)
        
        name_list=[]
        list_=[]
        mess_list=[]  
        i=1
        for s in tup:
            index=s.find("###")
            if index!=-1:
                name_list.append((str(i)+"."+str(0),str(i)+"."+str(index)))
                list_.append((str(i)+"."+str(index), str(i)+"."+str(index+3)))
                index+=3
                relis=get_index(s,i,index)
                if relis:
                    mess_list.append(relis)
                else:
                    mess_list.append((str(i)+"."+str(index), str(i)+"."+str(index+len(s[index::]))))
            i+=1
        for name in name_list:
            text.tag_add("name",name[0],name[1])
        for a in list_:
            text.tag_add("#",a[0],a[1])
        for mess in mess_list:
            if type(mess)==tuple:
                text.tag_add("mess",mess[0],mess[1])
            else:
                for m in mess:
                    text.tag_add("mess",m[0],m[1])
        text.tag_config("name", foreground=self.Color['name'])
        text.tag_config("#",foreground=self.Color['#'])  
        text.tag_config("mess",foreground=self.Color['mess'])  
    
    def savetext(self,):
        print(Spilt_Mess.Isfile(self.textlab['text']))
        if Spilt_Mess.Isfile(self.textlab['text']) == ".jpg" or Spilt_Mess.Isfile(self.textlab['text']) == ".png" or Spilt_Mess.Isfile(self.textlab['text']) == ".gif" or not self.textlab['text']:
            return
        if os.path.isfile(self.textlab['text']):
            file=open(self.textlab['text'],"w")
            text=self.pantext.get("0.0","end")
            i=len(text)-1
            if text[i] != '\n':
                file.write(text+'\n')
                file.write(text[0:i+2:])
                file.close()
                return
            while text[i]=='\n':
                i-=1
            file.write(text[0:i+2:])
            file.close()
    
    def check_file(self,event):
        tup = self.pancanv.find_closest(event.x, event.y)
        index = self.pan_tag.index(tup[0])
        name=self.setstr4[index]
        self.panframe.add(self.panson)
        if os.path.isdir(name):
            self.open_other(name)
        elif os.path.isfile(name):
            self.opentext(name)
        
    def opentext(self,name):
        try:
            self.savetext() 
        except:
            pass
        self.pantext.delete("0.0", "end")  
        self.textlab.config(text=name)        
        file=open(name,"r")
        s=file.read()
        file.close()
        self.color_insert(self.pantext,s)
        
    def openpic(self,name):
        self.textlab.config(text=name)  
        self.pantext.delete("0.0", "end")  
        self.atpic=tk.PhotoImage(file=name)
        self.pantext.image_create("end",image=self.atpic)
    
    def open_other(self,name):
        name=f.askopenfilename(initialdir=name,)
        type=Spilt_Mess.Isfile(name)
        if type==".png" or type==".gif":
            self.openpic(name)
        elif type=='.jpg':
            name=Spilt_Mess.totos(name,(self.Win_Size[0][0],self.Win_Size[0][1]))
            self.openpic(name)
        else:
            self.opentext(name)
        