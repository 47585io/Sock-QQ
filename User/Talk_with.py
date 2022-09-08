
from unittest.util import safe_repr
from User.Friend import*
from Pubilc.Split import Spilt_Mess
from User.UDPmess import th
from User.History import History

class Talk_with(Friend_list):
    '''the talk_with class, can talk with your friens or grounp, and send or get file'''

    def __init__(self) -> None:
        Friend_list.__init__(self)
        self.talk = th.Thread(target=self.Readshow,)
        self.talk.setDaemon(True)
        self.istalk = 0
        #Always check whether has a mess to display
    
    def init(self):
        Friend_list.init(self)
        self.history=History()
        self.topinit()
  
    def quickconfig(self, friends, mess, sock, tcpmess, tcpsock):
        Friend_list.quickconfig(self, friends, sock, mess)
        self.tcpmess = tcpmess
        self.tcpsock = tcpsock
        self.win2.overrideredirect(True)
        self.topconfig(self.toplab,(self.topbut,self.topxbut),self.toplist,self.topscro)
        self.topclose()
        #used for send and get file
        
    def topclose(self):
        self.win2.geometry("0x0-1000-1000")
    
    def Login(self):   
        self.mess.init(self.User_Name,self.filename,self.tcpmess)
        self.mess.Send(self.sock,"LOGIN "+self.User_Name)
        self.tcpmess.Add_a_Send("Server",self.User_Name,self.filename)
        self.history.refuall(self.fren)
        super().Login()
        
    def chu(self, new):
        '''get friend headpic from server, add to a dir and add to self.fren.pic with name'''
        s_str = []
        i=0
        self.mess.Send(self.sock,"GetHead "+str(new))
        #init a GetHead str and send to udpmess server, and server return a headpic list
        head_str=self.mess.getSpecial()
        #get the new mess
        head_lis=Spilt_Mess.Friend_list_Read_Spilt(head_str)
        #use Friend_list_Read_Spilt, cut str to list:[headname1,...]
        while i<len(head_lis):
            s_str.append(Spilt_Mess.Get_mess_spilt("Server",new[i],head_lis[i]))
            i+=1
        #from list get a pic every once, and add in s_str list(a going to get file list)
        self.getfile(s_str)
        #get all, and save in ./mydir/Server/picname
        i=0
        while i<len(head_lis):
            self.fren.pic.append(self.tcpmess.mydir+"Server/"+head_lis[i])
            i+=1
        #get name in new list, and Find from the corresponding head_lis
        #end, add the file path to self.fren.pic
    
    @staticmethod
    def small(num):
        if num<1:
            return 1
        else:
            return num
    
    def Closeall(self):
        '''when user close the window, saveall and exit'''
        self.isstart=0
        sleep(0.5)
        self.history.saveall(self.fren)
        exit(0)
    
    def talk_with(self, name):
        '''config a talk page'''
        if self.istalk == 0:
            self.talk.start()
            self.istalk += 1  
                
        self.but_list[1].config(command=lambda: self.retu(self.endretu))
        self.but_list[4].config(command=lambda :self.refresh(self.endretu))
        self.fren.talk_with = name
        self.win.title("Talk_With - "+"("+self.fren.talk_with+")")
        self.f_scro.pack(fill=tk.Y, side='right')
        self.f_can.config(
            height=self.Win_Size[0][1]-75, width=self.Win_Size[0][0])
        self.f_can.configure(scrollregion=(0,0,500,0))
        self.f_can.yview_moveto(1.0)
        self.f_can.pack()
        
        self.entfarme.pack(side='left', anchor='nw')
        self.but_list[2].config(
            text='Send', command=lambda: self.Sendshow(0, name, self.ent.get()))
        self.but_list[2].pack(side='left')
        self.ent.bind("<Return>", lambda x,
                      y=name: self.Sendshow(x, y, self.ent.get()))
        
        self.but_list[0].config(command=self.sendfile, text="↑",width=1)
        self.but_list[3].config(text="↓",width=1,command=self.usergetfile)
        self.but_list[3].place(x=self.Win_Size[0][0]-35, y=0)
        self.but_list[0].place(x=self.Win_Size[0][0]-60, y=0)
        
        self.refumess(name)
        
    def Sendshow(self, tmp, name, s_str):
        '''when user send a str, immediately show and send to other user'''
        if name != "my shadow" or name != "my computer":
            self.mess.Send(self.sock, s_str, name)
        self.draw_a_friend(self.f_can, s_str, self.furry_l[0],
                           (self.Canv_x+30, self.Canv_y, self.Win_Size[0][0]-self.pic_size[0], self.Canv_y+self.small(len(s_str)//26)*50,),  (self.Canv_x+205, self.Canv_y+self.small(len(s_str)//26)*10*2+2,), (self.Win_Size[0][0]-self.pic_size[0]+50, self.Canv_y+45,), self.delmess, self.Color['bubu1'])
        self.Canv_y += self.pic_size[1]+25 if self.pic_size[1] > self.small(len(s_str)//26)*50 else self.small(len(s_str)//26)*50+25
        if self.Canv_y > self.Win_Size[0][1]:
            self.f_can.configure(scrollregion=(
                0, 0, 500, self.Canv_y-self.Win_Size[0][1]+self.pic_size[1]))
            self.f_can.yview_moveto(1.0)
        
        self.history.put_a_mess(name,Spilt_Mess.Sava_Self_mess(s_str))
  #one way or another, save the mess waiting for use
        
    def Readshow(self):
        '''get a mess from UDPmess, and spilt'''
        print("start Readshow")
        while 1:
            s_str = self.mess.get()
            if s_str: 
    #when server exit, then after the mess, no mess read
    #if want to connet, wait server start  and send any mess to server and wait read  
                if s_str.decode()=="EXIT":
                    print("服务端已退出")
                    continue
                s, name = Spilt_Mess.Read_spilt(s_str)
                
    #if this is a file mess, go to save the mess, i use it get file from server after save, and it is From who to me
                lis=Spilt_Mess.File_spilt(s.encode())
                if lis!=0:
                    if name not in self.history.File_all:
                        self.history.File_all[name]=[]
                    self.history.File_all[name].append(Spilt_Mess.Get_mess_spilt(
                        lis[0], lis[1], lis[2]))
                    continue

    #if not, go to display on talking with user Canvas, talk out, then save it in messcache          
                if name == self.fren.talk_with:
                    i = self.fren.friend_list.index(name)
                    self.draw_a_friend(self.f_can, s, self.furry_l[i], (self.Canv_x, self.Canv_y, self.Win_Size[0][0]-30, self.Canv_y+self.pic_size[1]-20,), (
                        self.Canv_x+self.pic_size[0]+self.Canv_x_from, self.Canv_y+25), (self.Canv_x+50, self.Canv_y+45,), self.delmess, self.Color['bubu2'])
                    self.Canv_y += self.pic_size[1]+25

    #when mess is end, move the Canvas
                    if self.Canv_y > self.Win_Size[0][1]:
                        self.f_can.configure(scrollregion=(
                            0, 0, 500, self.Canv_y-self.Win_Size[0][1]+self.pic_size[1]))
                        self.f_can.yview_moveto(1.0)
                
                self.history.put_a_mess(name,s)
                #save
                
    def getfile(self, s_str):
        '''put s_str list in tcpmess spilt list and wait spilt'''
        for s in s_str:
            self.tcpmess.Add_a_Get(s)

    def sendfile(self):
        '''add go to send file'''
        filename = fid.askopenfilenames()
        for file in filename:
            if os.path.isdir(file):
                filelist=os.listdir(file)
                for f in filelist:
                    self.tcpmess.Add_a_Send(
                        self.User_Name, self.fren.talk_with, f)
            else:
                self.tcpmess.Add_a_Send(self.User_Name, self.fren.talk_with, file)
            self.Sendshow(0, self.fren.talk_with, Spilt_Mess.Send_mess_spilt(
                self.User_Name, self.fren.talk_with, file, str(os.path.getsize(file))).decode())
    #upload file to server, and send command string to get file to user, wait user get it
    
    def usergetfile(self,):
        '''from history.file, get talk_with send to str, and send to server get the file'''
        self.toplist.delete(0,"end")
        tup=self.geostr(self.win.geometry(),("x","+","+"))
        s=self.geosize((self.Win_Size[1][0], self.Win_Size[1][1], tup[0]+tup[2], tup[3]))
        self.win2.geometry(s)
        #sonwindow Always follow parent window
        
        self.toplist.config(height=8, width=16)
        self.topbut.config(anchor='nw',text="Get", command=self.cursor)
        
        try:
            for mess in self.history.File_all[self.fren.talk_with]:
                file=Spilt_Mess.File_spilt(mess)
                self.toplist.insert("end",file[2])
        except Exception as e:
            print(e)
        #show friend send's command string, and choose and get the file
        self.win2.update()
        
    def cursor(self):
        '''Add the file command string to be obtained to the tcp list through user options and wait for it to be obtained'''
        tup=self.toplist.curselection()
        lis=[]
        for t in tup:
            lis.append(self.history.File_all[self.fren.talk_with][t])
        self.getfile(lis)
            
    def endretu(self):
        '''clear Canvs'''
        self.clear_Canv()
        self.topclose()
        self.but_list[0].place_forget()
        self.but_list[3].place_forget()
    
    def delmess(self,event):
        pass

    def refumess(self,name):
      '''when user talk with friend, refu history mess'''
      try:
        i = self.fren.friend_list.index(name)
        for mess in self.history.Mess_Friend[self.fren.talk_with]:
            if mess.startswith("MY#"):
                self.draw_a_friend(self.f_can,mess, self.furry_l[0],
                                   (self.Canv_x+30, self.Canv_y, self.Win_Size[0][0]-self.pic_size[0], self.Canv_y+self.small(len(mess)//26)*30+20,),  (self.Canv_x+205, self.Canv_y+self.small(len(mess)//26)*10*2+2,), (self.Win_Size[0][0]-self.pic_size[0]+50, self.Canv_y+45,), self.delmess, self.Color['bubu1'])
                self.Canv_y += self.pic_size[1]+25 if self.pic_size[1] > self.small(
                    len(mess)//26)*30+20 else self.small(len(mess)//26)*30+45
                
            else:
                self.draw_a_friend(self.f_can, mess, self.furry_l[i], (self.Canv_x, self.Canv_y, self.Win_Size[0][0]-30, self.Canv_y+self.pic_size[1]-20,), (
                    self.Canv_x+self.pic_size[0]+self.Canv_x_from, self.Canv_y+10), (self.Canv_x+50, self.Canv_y+45,), self.delmess, self.Color['bubu2'])
        #if mess is myself, is put right, if not, put on left
          
            if self.Canv_y > self.Win_Size[0][1]:
                self.f_can.configure(scrollregion=(
                0, 0, 500, self.Canv_y-self.Win_Size[0][1]+self.pic_size[1]))
            self.f_can.yview_moveto(1.0)
        #move Canvas
      except Exception as e:
          print(e)

        