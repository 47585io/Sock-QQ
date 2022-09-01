import socket
from Pubilc.Split import Spilt_Mess
from User.Friend import Th
Mess_Buffer = 1024

TCP_SOCK = socket.socket()
TCP_SOCK.bind(("", 0))
# the user, olny two port with server

class TCP_mess:
    def __init__(self,sock=TCP_SOCK) -> None:
        self.sendfile_list=[]
        self.readfile_list=[]
        self.slinepool=Th(2)
        self.sock=sock
        self.issend=0
        self.isread=0
    def Sendfile(self,addr=("127.0.0.1",1237)):
        for file in self.sendfile_list:
            self. sock.connect(addr)
            self.sock.recv()
        
    def Add_a_Send(self,From,To,filename):
        s_str=Spilt_Mess.Send_mess_spilt(From, To, filename)
        self.sendfile_list.append(s_str)
        self.Sendfile
        pass
TCP = TCP_mess()