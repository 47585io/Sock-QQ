import socket
import os
from Pubilc.Split import Spilt_Mess
from User.Friend import Th
Mess_Buffer = 512
MY_DIR="./mydir/"

TCP_SOCK = socket.socket()
TCP_SOCK.bind(("", 0))
# the user, olny two port with server

class TCP_mess:
    '''used for send and get file class'''
    def __init__(self,sock=TCP_SOCK) -> None:
        self.sendfile_list=[]
        #every element is a tuple:(str,srcfile)
        self.getfile_list=[]
        #every element is a tupr: (getfilestr,filename,fromwho)
        self.slinepool=Th(2)
        self.sock=sock
        self.issend=0
        self.isget=0
#work In the background,
        self.mydir = MY_DIR
        if not os.path.isdir(self.mydir):
            os.mkdir(self.mydir)
            
    def Sendfile(self,addr=("192.168.1.3",1237)):
        '''deal with sendfile in list, when Finish, return and clear sended file str'''
        self.issend=1
        print("Send")
        for file in self.sendfile_list:
#send a file to server
            sock=socket.socket()
            sock.connect(addr)
            print("connect!")
#connect           
            sock.send(file[0])
            size = os.path.getsize(file[1])
            fileobj=open(file[1],"rb")
            sock.recv(Mess_Buffer)
#you must recv a mess, for wait server
            while size>0:
                date=fileobj.read(Mess_Buffer)
                sock.send(date)
                size-=Mess_Buffer
            fileobj.close()
            sock.recv(Mess_Buffer)
            print("Send finish")
            sock.close()
#before close, wait server finish
        self.issend=0  
        self.sendfile_list.clear()
#clear all send str
    
    def Getfile(self,addr=("192.168.1.3", 1237)):
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
            fileobj = open(self.mydir+file[2]+"/"+file[1], "wb")
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
        if not filename:
            return
        s_str = Spilt_Mess.Send_mess_spilt(From, To, filename, str(os.path.getsize(filename)))
        self.sendfile_list.append((s_str,filename))
        if self.issend==0:
            self.slinepool.submit(self.Sendfile)

    def Add_a_Get(self, Getstr):
        '''get a file from server(add it in list)'''
        print("Get")
        lis=Spilt_Mess.File_spilt(Getstr)
        filename=lis[2]
        fromwho=lis[0]
        if not os.path.isdir(self.mydir+fromwho):
            os.mkdir(self.mydir+fromwho)
        self.getfile_list.append((Getstr,filename,fromwho))
        if self.isget == 0:
            self.slinepool.submit(self.Getfile)

TCP = TCP_mess()