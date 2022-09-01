import threading as th
from Pubilc.Split import Spilt_Mess
import socket
Mess_Buffer = 1024
Max_Mess = 10
# recv buffer size and user mess_list size
from User.Welcome import USER_NAME
MAX_THD = 1
UDP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_SOCK.bind(("", 0))

class UDP_Mess:
    def __init__(self,sock=UDP_SOCK) -> None:
        self.sock=sock
        for i in range(MAX_THD):
            r = th.Thread(target=self.Read, args=(self.sock,))
            r.setDaemon(True)
            r.start()
        self.MessCache = []
        self.index = -1
        self.yes = 0
# Mess list: Max 10 mess,  index: now new mess index, yes:the mess yes or on new mess

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

    def Send(self, sock, send_str, to_user=None, to_addr=("127.0.0.1", 1234)):
        '''when want send mess to server, call it'''
        self.yes = 0
        # when send a mess, Read going to read a new mess, the yes=0, now index is no new
        send_str = Spilt_Mess.Send_spilt(send_str, to_user)
        sock.sendto(send_str, to_addr)

    def Read(self, sock):
        '''every once, recv a mess and add it to MessCache, if mess count >Max, del old mess'''
        global USER_NAME
        while 1:
            tmp = sock.recvfrom(Mess_Buffer)
            self.MessCache.append(tmp[0])
            self.index += 1
            self.yes = 1
            if(self.index >= Max_Mess):
                del self.MessCache[0]
                self.index -= 1
            print("i am ", USER_NAME, "a new mess: ", tmp[0], "\n")


UDP = UDP_Mess()
# mess object
