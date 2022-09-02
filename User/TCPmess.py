import socket
import os
from Pubilc.Split import Spilt_Mess
from User.Friend import Th
Mess_Buffer = 1024

TCP_SOCK = socket.socket()
TCP_SOCK.bind(("", 0))
# the user, olny two port with server

class TCP_mess:
    '''used for send and get file class'''
    def __init__(self,sock=TCP_SOCK) -> None:
        self.sendfile_list=[]
        #every element is a tuple:(str,srcfile)
        self.getfile_list=[]
        #every element is a tupr: (getfilestr,filename)
        self.slinepool=Th(2)
        self.sock=sock
        self.issend=0
        self.isget=0
#work In the background,   
        if not os.path.isdir("./mydir"):
            os.mkdir("./mydir")
            
    def Sendfile(self,addr=("127.0.0.1",1237)):
        '''deal with sendfile in list, when Finish, return and clear sended file str'''
        self.issend=1
        print("Send")
        for file in self.sendfile_list:
#send a file to server
            sock=socket.socket()
            sock.connect(addr)
            print("connect!")
            sock.send(file[0])
            size = os.path.getsize(file[1])
            fileobj=open(file[1],"rb")
            while size>0:
                date=fileobj.read(Mess_Buffer)
                sock.send(date)
                size-=Mess_Buffer
            fileobj.close()
            sock.recv(Mess_Buffer)
            print("Send finish")
            sock.close()
        self.issend=0  
        self.sendfile_list.clear()
    
    def Getfile(self,addr=("127.0.0.1", 1237)):
        '''deal with file in list, when finish, return and clear geted file str'''
        print("get")
        self.isget= 1
        for file in self.getfile_list:
#get a file and save in default dir
            sock=socket.socket()
            sock.connect(addr)
            print("connect")
            sock.send(file[0])
            s=sock.recv(Mess_Buffer)
            size=int(s.decode())
            fileobj = open("./mydir/"+file[2]+"/"+file[1], "wb")
            sock.send("Ok".encode())
            while size > 0:
                date=sock.recv(Mess_Buffer)
                fileobj.write(date)
                size -= Mess_Buffer
            fileobj.close()
            sock.send("Ok".encode())
            print("get finish")
            sock.close()
        self.isget = 0
        self.getfile_list.clear()
        
    def Add_a_Send(self,From,To,filename):
        '''send a file to server'''
        s_str = Spilt_Mess.Send_mess_spilt(From, To, filename, str(os.path.getsize(filename)))
        self.sendfile_list.append((s_str,filename))
        if self.issend==0:
            self.slinepool.submit(self.Sendfile)

    def Add_a_Get(self, Getstr):
        '''get a file from server(add it in list)'''
        lis=Spilt_Mess.File_spilt(Getstr)
        filename=lis[2]
        fromwho=lis[1]
        if not os.path.isdir("./mydir/"+fromwho):
            os.mkdir("./mydir/"+fromwho)
        self.getfile_list.append((Getstr,filename,fromwho))
        if self.isget == 0:
            self.slinepool.submit(self.Getfile)

TCP = TCP_mess()