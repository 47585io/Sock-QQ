
from User.Friend import*
from Pubilc.Split import Spilt_Mess
from User.UDPmess import th


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

    def quickconfig(self, friends, mess, sock, tcpmess, tcpsock):
        Friend_list.quickconfig(self, friends, sock, mess)
        self.tcpmess = tcpmess
        self.tcpsock = tcpsock
        #used for send and get file

    def talk_with(self, name):
        '''config a talk page'''
        if self.istalk == 0:
            self.talk.start()
            self.istalk += 1

        self.but_list[0].config(command=self.sendfile, text="↑↓")
        self.but_list[0].pack()

        self.but_list[1].config(command=lambda: self.retu(self.clear_Canv))
        self.fren.talk_with = name
        self.f_scro.pack(fill=tk.Y, side='right')
        self.f_can.config(
            height=self.Win_Size[0][1]-78, width=self.Win_Size[0][0])
        self.f_can.pack()
        self.entfarme.pack(side='left', anchor='nw')
        self.but_list[2].config(
            text='Send', command=lambda: self.Sendshow(0, name, self.ent.get()))
        self.but_list[2].pack(side='left')
        self.ent.bind("<Return>", lambda x,
                      y=name: self.Sendshow(x, y, self.ent.get()))

    def Sendshow(self, tmp, name, s_str):
        '''when user send a str, immediately show and send to other user'''
        if name != "my shadow" or name != "my computer":
            self.mess.Send(self.sock, s_str, name)
        self.draw_a_friend(self.f_can, s_str, self.furry_l[0],
                           (self.Canv_x+30, self.Canv_y, self.Win_Size[0][0], self.Canv_y+self.pic_size[1]-20,),  (self.Canv_x+20, self.Canv_y+10,), (self.Win_Size[0][0]-self.pic_size[0]+50, self.Canv_y+45,), self.delmess, self.Color['bubu1'])
        self.Canv_y += self.pic_size[1]+10
        if self.Canv_y > self.Win_Size[0][1]:
            self.f_can.configure(scrollregion=(
                0, 0, 500, self.Canv_y-self.Win_Size[0][1]+self.pic_size[1]))
            self.f_can.yview_moveto(1.0)

    def Readshow(self):
        '''get a mess from UDPmess, and spilt'''
        while 1:
            s_str = self.mess.get()
            if s_str:    
                s, name = Spilt_Mess.Read_spilt(s_str)
                
    #if this is a file mess, go to save the mess, i use it get file from server after save, and it is From who to me
                lis=Spilt_Mess.File_spilt(s.encode())
                if lis!=0:
                    self.fren.File_all[str(lis[0])]=Spilt_Mess.Get_mess_spilt(
                        lis[0], lis[1], lis[2])
                    continue
    
    #if not, go to display on talking with user Canvas, talk out, then save it in messcache          
                print("this ", name, "   ", s, "\n")
                #self.fren.Mess_Friend[name].append(s)
                if name == self.fren.talk_with:
                    i = self.fren.friend_list.index(name)
                    self.draw_a_friend(self.f_can, s, None, (self.Canv_x, self.Canv_y, self.Win_Size[0][0]-30, self.Canv_y+self.pic_size[1]-20,), (
                        self.Canv_x+self.pic_size[0]+self.Canv_x_from, self.Canv_y+10), (self.Canv_x+50, self.Canv_y+45,), self.delmess, self.Color['bubu2'])
                    self.Canv_y += self.pic_size[1]+10
    
    #when mess is end, move the Canvas
                    if self.Canv_y > self.Win_Size[0][1]:
                        self.f_can.configure(scrollregion=(
                            0, 0, 500, self.Canv_y-self.Win_Size[0][1]+self.pic_size[1]))
                        self.f_can.yview_moveto(1.0)

    def getfile(self, s_str):
        
        pass

    def sendfile(self):
        '''add go to send file'''
        filename = fid.askopenfilenames()
        for file in filename:
            self.tcpmess.Add_a_Send(self.User_Name, self.fren.talk_with, file)
            self.Sendshow(0, self.fren.talk_with, Spilt_Mess.Send_mess_spilt(
                self.User_Name, self.fren.talk_with, file, str(os.path.getsize(file))).decode())

    def delmess(self,event):
        
        
        
        pass
