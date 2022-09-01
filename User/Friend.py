from User.Welcome import*

# the class can't to new class!!!!
# or, try lab?
# no! it not have scro!
# but we must 继承 baseclass, 否则 all lab going to del
# why?.... why not?


class Friend_list(Welcome):
    '''the friend_list class, can show your friend_list and add new friend'''

    def __init__(self) -> None:
        Welcome.__init__(self)
        self.Canv_x = 0  # 50
        self.Canv_y = 0  # 45
        self.Canv_x_from = 70
        self.Canv_size = (self.Win_Size[0][0], self.pic_size[1])
        self.s = th.Thread(target=self.search,)
        self.s.setDaemon(True)
        self.isstart = 0

    def init(self,):
        '''redefine func'''
        Welcome.init(self)
        self.canv_init()
        self.furry_l = []
        self.tag_list = []
        self.List = tk.Listbox(self.bgfarme, background=self.Color['bg'], selectbackground=self.Color['ffg'],
                               foreground=self.Color['fg'], selectforeground=self.Color['fg'], borderwidth=0, highlightthickness=0)

    def canv_init(self,):
        '''init canv and scro'''
        # self.canfarme=tk.Frame(self.bgfarme)
        self.f_can = tk.Canvas(self.bgfarme, highlightthickness=0, confine=False, background=self.Color['bg'], selectbackground=self.Color['ffg'], selectforeground='white', borderwidth=0,)
        self.f_scro = tk.Scrollbar(self.bgfarme)

    def canvconfig(self, canv, scro):
        '''config a Canv with Theme'''
        canv.config(width=self.Win_Size[0][0]-1, height=self.Win_Size[0]
                    [1]-1, borderwidth=0, yscrollcommand=scro.set,)
        scro.config(command=canv.yview, background=self.Color['fg'],
                    activebackground=self.Color["entblock"], borderwidth=0, elementborderwidth=0, activerelief="sunken")
        canv.configure(scrollregion=(0,0,500,len(self.furry_l)*self.pic_size[1]))
        canv.yview_moveto(0.0)
    def quickconfig(self, friends, sock, mess):
        '''redefine func'''
        Welcome.quickconfig(self, mess, sock)
        self.fren = friends
    def new(self):
        '''redefine last class func, go to show friends'''
        self.Win_Size[0][0]+=100
        self.Win_Size[0][1]+=200
        self.win.geometry(self.geosize())
        self.bgfarme.config(
            background=self.Color["bg"], width=self.Win_Size[0][0], height=self.Win_Size[0][1])
        self.go(self.showfriends)
        pass

    def place_forgets(self, *arg):
        '''it going to place_forget all arg as mid fun before pack_forget'''
        for a in arg:
            a.place_forget()

    def draw_a_friend(self, canv, name, pic, relapos, namepos, picpos, func, color="#282c34"):
        '''draw a friend mess'''      
        tag = canv.create_rectangle(relapos[0], relapos[1], relapos[2], relapos[3], fill=color,
                                    activefill=self.Color['ffg'], outline=self.Color['bg'], width=0)
        if canv:
            canv.create_image(picpos[0], picpos[1], image=pic,)
        canv.create_text(namepos[0]+40, namepos[1], width=relapos[2]-relapos[0]-picpos[1]+picpos[0],
                         text=name, fill=self.Color['fg'], font=(self.Font["zheng"], self.Font_size["mid"]))
        self.f_can.tag_bind(tag, '<Button-1>', func)
        self.tag_list.append(tag)

    def showfriends(self):
        self.canvconfig(self.f_can, self.f_scro)
        self.but_list[0].config(text="+", command=self.addfriend_mid)
        self.but_list[0].place(x=self.Win_Size[0][0]-40, y=0)
        self.f_scro.pack(fill=tk.Y, side='right')
        self.f_can.pack()

    # but_list[0] is place!!!

        if self.fren.pic == []:
            self.f_can.create_text(self.Win_Size[0][0]//2, self.Win_Size[0][1]//2-50, fill=self.Color['fg'], font=(
                self.Font["zheng"], self.Font_size["big"], "bold"), text="No Friends!")

        count = len(self.furry_l)
        while count < len(self.fren.show()):
            if count >= len(self.fren.pic):
                self.furry_l.append(tk.PhotoImage(
                    file="./picture/default.png", width=self.pic_size[0], height=self.pic_size[1]))
            else:
                self.furry_l.append(tk.PhotoImage(
                    file=self.fren.pic[count], width=self.pic_size[0], height=self.pic_size[1]))
            count += 1
        for count in range(len(self.furry_l)):
            if count % 2 == 0:
                self.draw_a_friend(
                    self.f_can, self.fren.friend_list[count], self.furry_l[count], (self.Canv_x, self.Canv_y, self.Win_Size[0][0], self.Canv_y+self.pic_size[1],), (self.Canv_x+self.pic_size[0]+self.Canv_x_from, self.Canv_y+self.pic_size[1]//2,), (self.Canv_x+50, self.Canv_y+45,), self.talk_with_mid)
            if count % 2 == 1:
                self.draw_a_friend(
                    self.f_can, self.fren.friend_list[count], self.furry_l[count], (self.Canv_x, self.Canv_y, self.Win_Size[0][0], self.Canv_y+self.pic_size[1],), (self.Canv_x+self.pic_size[0], self.Canv_y+self.pic_size[1]//2,), (self.Win_Size[0][0]-self.pic_size[0]+50, self.Canv_y+45,), self.talk_with_mid)
            count += 1
            self.Canv_y += self.pic_size[1]
            # print(self.Canv_x)

    def addfriend_mid(self):
        '''clear Canv and go to add friend'''
        self.clear_Canv()
        self.go(self.addfriend, self.showfriends,
                lambda: self.place_forgets(self.but_list[0]))

    def addfriend(self):
        '''config a addfriend page'''
        self.entfarme.pack()
        self.List.pack()
        self.but_list[2].pack(side='right')
        self.but_list[2].config(text='Ok', font=(
            self.Font["zheng"], self.Font_size['mid']+3,), command=self.addmany)
        self.fren.addfriend(self.mess, self.sock)
        if self.isstart == 0:
            self.isstart += 1
            self.s.start()

    def search(self):
        '''search user input str in friend_list'''
        tmp = ""
        while 1:
            if tmp == self.ent.get():
                continue
            tmp = self.ent.get()
            if not tmp:
                self.List.delete(0, "end")
            list = self.fren.Search_Friend(self.ent.get())
            if list:
                self.List.delete(0, "end")
                for l in list:
                    self.List.insert("end", l)
            else:
                self.List.delete(0, "end")

    def addmany(self):
        '''user going to add friend'''
        try:
            tup = self.List.get(self.List.curselection())
            new = self.fren.format_list(tup)
            if new:
                self.fren.friend_list.append(new)
        except Exception:
            pass

    def clear_Canv(self,):
        '''clear Canv on old page'''
        self.f_can.delete(tk.ALL)
        #self.index = 0
        self.tag_list.clear()
        self.Canv_y = 0
        # self.furry_l.clear()

    def talk_with_mid(self, event):
        '''user choose which friend'''
        #print(event.widget, event.x, event.y)
        tup = self.f_can.find_closest(event.x, event.y)
        index = self.tag_list.index(tup[0])
        name = self.fren.friend_list[index]
        self.clear_Canv()
        self.go(lambda: self.talk_with(name), self.showfriends,
                lambda: self.place_forgets(self.but_list[0]))

    def talk_with(self, name):
        print(name)
    # please redefine after
