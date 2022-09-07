import socket
import os
from Server.users import users
from Pubilc.Split import Spilt_Mess
Mess_Buffer = 128
# 设置每一个sock cache buffer size

class message:
    '''read and process and send user send's mess'''
#you can put a dict in queue
#the mess server can on many port, but it olny init users once, so their share queue
#a port can have many process, the same port's process will fight date, but their space is different, so if once process get user name and addr,must save in queue

    def __init__(self, tup=("127.0.0.1", 1234)) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(tup)
        self.USERS = users()

    def bbmess(self, tmp):
        '''process going to send str'''
        
        lis = []
        my_name=self.USERS.value_to_key(tmp[1])
        
    #if user login, call login get cache, the end , send mess to src user
        if tmp[0].decode().startswith("LOGIN"):
            cache = self.USERS.Login(tmp)
            for mess in cache:
                self.Send((mess.encode(),tmp[1]))
                   
    #if user exit, del it in now_in
        elif tmp[0].decode().startswith("EXIT"):
            self.USERS.exit(tmp[1])

        #if user want to addfriend, return the users name
        elif tmp[0].decode().startswith("AddFriend"):
            lis.append(Spilt_Mess.Send_spilt(self.USERS.get_friend_list(),my_name))
            lis.append(tmp[1])
            return lis
    
    #user want get friends head, spilt str, search filename and return 
        elif tmp[0].decode().startswith("GetHead"):
            name_list=Spilt_Mess.Friend_list_Read_Spilt(tmp[0])
            head_lis=[]
            self.USERS.addgroupfriend(my_name,name_list)
            
    #if want add a groupfriend, add it to the group's friend_list
            for name in name_list:
                nametmp=os.listdir("./From/Server/"+name)
                head=nametmp[0]
                head_lis.append(head)
            s=Spilt_Mess.Friend_list_Send_Spilt(head_lis).decode()
            lis.append(Spilt_Mess.Send_spilt(s,my_name))
            lis.append(tmp[1])
            return lis
               
    #default, the mess is name@str, read it , get the str and name, send str to name, and add mess from(my_name@str)
    #so send my_name@str to name's addr
        else:
            s_str, name = Spilt_Mess.Read_spilt(tmp[0])
            if name in self.USERS.getto(self.USERS.group):
                self.Sendall(s_str,my_name,name)
                return 
            else:
              if self.USERS.Isin(s_str,name,tmp[1]):
                addr = self.USERS.getto(self.USERS.users, name)
                name = self.USERS.value_to_key(tmp[1])
                s_str = Spilt_Mess.Send_spilt(s_str, name)
                lis.append(s_str)
                lis.append(addr)
                return lis

    def talk_to(self, *arg):
        '''the talk_to going to recv a bytes mess from a user, after process, it send a bytes mess to other user'''
        while True:
            tmp = self.sock.recvfrom(Mess_Buffer)
            print("接收", tmp)
            lis = self.bbmess(tmp)
            print("发送", lis)
            self.Send(lis)

    def Send(self, lis):
        '''send bytes, can redefine in sonclass'''
        if not lis:
            return
        if not lis[1]:
            return
        self.sock.sendto(lis[0], lis[1])
        #the lis[0] is from@str, lis[1] is send to addr
    
    def Sendall(self,sendstr,fromwho,togroup):
        '''send a mess to all user in group'''
        friend_list=self.USERS.getto(self.USERS.friend_list,togroup)
        sendstr=Spilt_Mess.Send_spilt(sendstr,togroup)
        for f in friend_list:
            if f!=fromwho:
              if self.USERS.Isin(sendstr, f, fromwho):
                addr=self.USERS.getto(self.USERS.users,f)
                self.Send((sendstr,addr))

    #diffrent port's date, it olny give this port , all port's  process olny get itself port's date
    #but, queue still can share
    
    def totouser(self):
        '''Kick users in the order in the list'''
        users=self.USERS.getto(self.USERS.now_in)
        for user in users:
            self.Send(("EXIT".encode(),self.USERS.getto(self.USERS.users,user)))