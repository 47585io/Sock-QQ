
import threading as th
from Pubilc.Split import Spilt_Mess
import socket
Time_out = 5
#set recv mess time out, Prevent threads from getting stuck
Mess_Buffer = 128
Max_Mess = 50
# recv buffer size and user mess_list size
MAX_THD = 1
UDP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_SOCK.bind(("", 0))

class UDP_Mess:
    '''used for communication class'''
    def __init__(self, sock=UDP_SOCK) -> None:
        self.sock = sock
        self.server_is_start=0
        self.MessCache = []
        self.Special_Mess=[]
        self.index = -1
        self.Special_index=-1
        self.yes = 0
        for i in range(MAX_THD):
            r = th.Thread(target=self.Read, args=(self.sock,))
            r.setDaemon(True)
            r.start()
# Mess list: Max 10 mess,  index: now new mess index, yes:the mess yes or on new mess
# Special_Mess,save special mess

    def init(self,name):
        self.myname=name
        
    def get(self):
        '''the func pop a element from MessCache head, and return'''
        if self.index >= 0:
            mess = self.MessCache[0]
            del self.MessCache[0]
            self.index -= 1
            return mess
        return

    def getnew(self):
        '''get best new mess'''
        while self.yes == 0:
            pass
        self.yes = 0
        tmp = self.MessCache[self.index]
        del self.MessCache[self.index]
        self.index -= 1
        return tmp

    def getSpecial(self):
      while 1:
        if self.Special_index < len(self.Special_Mess) and self.Special_index>=0 and self.yes:
            tmp =self.Special_Mess[self.Special_index]
            del self.Special_Mess[self.Special_index]
            self.Special_index-=1
            return tmp

    def Send(self, sock, send_str, to_user=None, to_addr=("127.0.0.1", 1234)):
        '''when want send mess to server, call it'''
        self.yes = 0
        # when send a mess, Read going to read a new mess, the yes=0, now index is no new
        send_str = Spilt_Mess.Send_spilt(send_str, to_user)
        sock.sendto(send_str, to_addr)
#if you has many server port, also can use random.randint init a num in a range 

    def Read(self, sock):
        '''every once, recv a mess and add it to MessCache, if mess count >Max, del old mess'''
        print("start Read")
        while 1:
          try:
            if self.server_is_start==0:
                sock.settimeout(Time_out)
            tmp = sock.recvfrom(Mess_Buffer)
                
            if tmp[0].decode().startswith(self.myname+"@"):
                print('this is a special mess!')
                tup=Spilt_Mess.Read_spilt(tmp[0])
                self.Special_Mess.append(tup[0].encode())
                self.Special_index+=1
                self.yes = 1
            else:
                self.MessCache.append(tmp[0])
                self.index += 1
                self.yes = 1
                if self.index >= Max_Mess:
                    del self.MessCache[0]
                    self.index -= 1
                    
            print("a new mess: ", tmp[0], "\n")
            self.server_is_start=1
            self.sock.settimeout(None)
            if tmp[0].decode()=="EXIT":
                self.server_is_start=0
                
          except Exception as e:
            self.Special_Mess.append(None)
            self.Special_index += 1
            print(e)
            self.yes=1

UDP = UDP_Mess()
# mess object
