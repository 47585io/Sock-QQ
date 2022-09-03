import socket
import os
from Server.users import users
from Pubilc.Split import Spilt_Mess
Mess_Buffer = 8192
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
    #if user login, call login get username and friend_list, the end , send mess to src user
        if tmp[0].decode().startswith("LOGIN"):
            s = self.USERS.Login(tmp)
            lis.extend((Spilt_Mess.Send_spilt(s,my_name), tmp[1]))
            return lis

        #if user want to addfriend, return the users name
        elif tmp[0].decode().startswith("AddFriend"):
            lis.append(Spilt_Mess.Send_spilt(self.USERS.get_friend_list(),my_name))
            lis.append(tmp[1])
            return lis
    
    #user want get friends head, spilt str, search filename and return 
        elif tmp[0].decode().startswith("GetHead"):
            name_list=Spilt_Mess.Friend_list_Read_Spilt(tmp[0])
            head_lis=[]
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
        self.sock.sendto(lis[0], lis[1])
        #the lis[0] is from@str, lis[1] is send to addr
        #login return a decode str,OK,then let us to encode


class Group_Mess(message):
    '''the group also is a user, but it's in server, and it's port in 1236, it's friend is all user in group, it's now_in user is now_in group's user'''

    def __init__(self, messaddr=("127.0.0.1", 1236)) -> None:
        message.__init__(self, messaddr)

    def bbmess(self, tmp):
        lis = []
        print("Group!")
        s_str, groupname = Spilt_Mess.Read_spilt(tmp[0])
        namelist = self.USERS.getto(self.USERS.friend_list, groupname)
        addrlist = []
        for name in namelist:
            addrlist.append(self.USERS.users[name])
        myname = self.USERS.value_to_key(tmp[1])
        s_str = Spilt_Mess.Send_spilt(s_str, myname)
        lis.append(s_str)
        lis.append(addrlist)
        return lis

    def Send(self, lis):
        '''read bytes from a user, and send all user in the group'''
        s_str = lis[0]
        for user in lis[1]:
            self.sock.sendto(s_str, user)
    #diffrent port's date, it olny give this port , all port's  process olny get itself port's date
