import socket
import os
from Pubilc.Split import Spilt_Mess
from User.Friend import Th
from User.UDPmess import Mess_Buffer
from User.UDPmess import Time_out
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
        #every element is a tuple: (getfilestr,filename,fromwho)
        self.slinepool=Th(2)
        self.sock=sock
        self.issend=0
        self.isget=0
#work In the background,
        self.s_g_size=[0,0]
        self.mydir = MY_DIR
        if not os.path.isdir(self.mydir):
            os.mkdir(self.mydir)
            
    def Sendfile(self,addr=("127.0.0.1",1237)):
        '''deal with sendfile in list, when Finish, return and clear sended file str'''
        self.issend=1
        print("Send")
        for file in self.sendfile_list:
#send a file to server
            try:
                fileobj=None
                sock=socket.socket()
                sock.settimeout(Time_out)
                sock.connect(addr)
                print("connect!")
#connect           
                sock.send(file[0])
                size = os.path.getsize(file[1])
                resize=size
                fileobj=open(file[1],"rb")
                sock.recv(Mess_Buffer)
                sock.settimeout(None)
#you must recv a mess, for wait server
                while size>0:
                    if self.issend==0:
                        print("send return")
                        return
                    date=fileobj.read(Mess_Buffer)
                    sock.send(date)
                    size-=Mess_Buffer
                    self.s_g_size[0] = "Send "+file[1] +" 共有: "+str(resize)+", "+"余下: "+str(size)+" "

#Each time the transmission data is synchronized with the server
                fileobj.close()
                sock.settimeout(Time_out)
                sock.recv(Mess_Buffer)
                print("Send finish")
                self.s_g_size[0] = "Send finish"
                sock.close()
#before close, wait server finish
                index = self.sendfile_list.index(file)
                del self.sendfile_list[index]
            except:
                print("与服务端断开连接")
                self.s_g_size[0] ="error"
                sock.close()
                if fileobj:
                    fileobj.close()
        self.issend=0  
    
    def Getfile(self,addr=("127.0.0.1", 1237)):
        '''deal with file in list, when finish, return and clear geted file str'''
        print("get")
        self.isget= 1
        
        for file in self.getfile_list:
#get a file and save in default dir
            try:
                fileobj=None
                sock=socket.socket()
                sock.settimeout(Time_out)
                sock.connect(addr)
                print("connect")
            
                sock.send(file[0])
                s=sock.recv(Mess_Buffer)
                size=int(s.decode())
                resize=size
                fileobj = open(self.mydir+file[2]+"/"+file[1], "wb")
                sock.send("Ok".encode())

                while size > 0:
                    if self.isget==0:
                        print("get return")
                        return
                    date=sock.recv(Mess_Buffer)
                    fileobj.write(date)
                    size -= Mess_Buffer
                    self.s_g_size[1] = "Get "+file[1]+" 共有: "+str(resize)+", "+"余下: "+str(size)+" "
                fileobj.close()
                sock.send("Ok".encode())
                print("get finish")
                self.s_g_size[1] = "Get finish"
                sock.close()
            
                index=self.getfile_list.index(file)
                del self.getfile_list[index]
                
#defalut, every once get a file, and close all and del self.getfile_list[index]
#but, if timeout, server is not start, then can't del self.getfile_list[index]

            except Exception:
                print("与服务端断开连接")
                self.s_g_size[1] ='error'
                sock.close()
                if fileobj:
                    fileobj.close()
          
        self.isget = 0
        
    def Add_a_Send(self,From,To,filename):
        '''send a file to server'''
        print("Add a Send")
        if not filename:
            return
        s_str = Spilt_Mess.Send_mess_spilt(From, To, filename, str(os.path.getsize(filename)))
        self.sendfile_list.append((s_str,filename))
#spilt str, add to list, wait send,
#if send sline not start, start, if not, olny add
        if self.issend==0:
            self.slinepool.submit(self.Sendfile)

    def Add_a_Get(self, Getstr):
        '''get a file from server(add it in list)'''
        print("Add a Get")
        lis=Spilt_Mess.File_spilt(Getstr)
        filename=lis[2]
        fromwho=lis[0]
        if not os.path.isdir(self.mydir+fromwho):
            os.mkdir(self.mydir+fromwho)
        self.getfile_list.append((Getstr,filename,fromwho))
        if self.isget == 0:
            self.slinepool.submit(self.Getfile)

TCP = TCP_mess()