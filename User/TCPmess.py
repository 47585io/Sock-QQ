import socket
import os
from Pubilc.Split import Spilt_Mess
from User.Friend import Th
Mess_Buffer = 1024

TCP_SOCK = socket.socket()
TCP_SOCK.bind(("", 0))
# the user, olny two port with server

class TCP_mess:
    def __init__(self,sock=TCP_SOCK) -> None:
        self.sendfile_list=[]
        #every element is a tuple:(str,srcfile)
        self.getfile_list=[]
        #every element is a tupr: (getfilestr,filename)
        self.slinepool=Th(2)
        self.sock=sock
        self.issend=0
        self.isget=0
        if not os.path.isdir("./User"):
            os.mkdir("./User")
    def Sendfile(self,addr=("127.0.0.1",1237)):
        self.issend=1
        for file in self.sendfile_list:
            self.sock.connect(addr)
            self.sock.send(file[0])
            size = os.path.getsize(file[1])
            fileobj=open(file[1],"rb")
            while size>0:
                date=fileobj.read(Mess_Buffer)
                self.sock.send(date)
                size-=Mess_Buffer
            fileobj.close() 
        self.issend=0  
    
    def Getfile(self,addr=("127.0.0.1", 1237)):
        self.isget= 1
        for file in self.getfile_list:
            self.sock.connect(addr)
            self.sock.send(file[0])
            s=self.sock.recv(Mess_Buffer)
            size=int(s.decode())
            fileobj = open("./User/"+file[1], "wb")
            while size > 0:
                date=self.sock.recv(Mess_Buffer)
                fileobj.write(date)
                size -= Mess_Buffer
            fileobj.close()
        self.isget = 0
        
    def Add_a_Send(self,From,To,filename):
        '''send a file to server'''
        s_str = Spilt_Mess.Send_mess_spilt(From, To, filename, str(os.path.getsize(filename)))
        self.sendfile_list.append((s_str,filename))
        if self.issend==0:
            self.slinepool.submit(self.Sendfile)
    
    def Add_a_Get(self, Getstr):
        '''get a file from server'''
        lis=Spilt_Mess.File_spilt(Getstr)
        filename=lis[2]
        self.getfile_list.append((Getstr,filename))
        if self.isget == 0:
            self.slinepool.submit(self.Getfile)

TCP = TCP_mess()