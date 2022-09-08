from Server.UDPmess import Spilt_Mess
from Server.UDPmess import Mess_Buffer
from Server.UDPmess import socket
import os


class TCP_Mess:
    '''server TCPmess, send or save file'''
    def __init__(self, addr=("127.0.0.1", 1237)) -> None:
        self.sock = socket.socket()
        self.sock.bind(addr)
        self.sock.listen(20)
        if not os.path.isdir("./From"):
            os.mkdir("./From")

    def checkfile(self, tup):
        '''search a file or mkdir on server mkdir'''
        if not os.path.isdir("./From/"+tup[0]):
            os.mkdir("./From/"+tup[0])
        if not os.path.isdir("./From/"+tup[0]+"/"+tup[1]):
            os.mkdir("./From/"+tup[0]+"/"+tup[1])

    def sendfile(self, new_sock, addr, tup):
      '''if user want to get a file, i must send to he'''
      try:
        print("Send")
        self.checkfile(tup)
        if not os.path.isfile("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2]):
            return
        size = os.path.getsize("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2])
        file = open("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2], "rb")
        new_sock.send(str(size).encode())
#send filesize
        print("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2])
        new_sock.recv(Mess_Buffer)
#must wait user
        while size > 0:
            date = file.read(Mess_Buffer)
            new_sock.send(date)
            size -= Mess_Buffer
#must wait user         
        new_sock.recv(Mess_Buffer)
        print("Send Finsh!")
      except Exception as e:
        print("Sendfile Error: ",e)
        file.close()
      else:
        file.close()

    def savefile(self, new_sock, addr, tup):
      '''if user want to send a file to me, i must save it'''
      try:
        print("Save")
        self.checkfile(tup)
        file = open("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2], "wb")
        size=int(tup[3])
        print("i have a dream , is can save a file")
        new_sock.send('Ok'.encode())
#respond user
        while size>0:
            date = new_sock.recv(Mess_Buffer)
            file.write(date)
            size-=Mess_Buffer
            
        print("Save Finsh")
        new_sock.send("Ok".encode())
#respond user
      except Exception as e:
        print("Savefile Error: ",e)
        file.close()
      else:
        file.close()

    def talk_to(self, *arg):
        '''before do any thing, Let's see what it is'''
        while 1:
          try:
            print("waiting")
            new_sock, addr = self.sock.accept()
            s_str = new_sock.recv(Mess_Buffer)
            s_list = Spilt_Mess.File_spilt(s_str)
            if s_str.decode()[0:3:]=='Get':   
                self.sendfile(new_sock, addr, s_list)
            else:
                self.savefile(new_sock, addr, s_list)
            new_sock.close()
          except Exception as e:
            print("TCP port: 抓住了,但是没有事", e)
            new_sock.close()
      
      
      
