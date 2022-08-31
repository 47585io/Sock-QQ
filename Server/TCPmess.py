from Server.UDPmess import Spilt_Mess
from Server.UDPmess import Mess_Buffer
from Server.UDPmess import socket
import os


class TCP_Mess:
    def __init__(self, addr=("127.0.0.1", 1237)) -> None:
        self.sock = socket.socket()
        self.sock.bind(addr)
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
        self.checkfile(tup)
        if not os.path.isfile("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2]):
            return
        size = os.path.getsize("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2])
        file = open("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2], "rb")
        new_sock.send('Ok'.encode())
        print("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2])
        while size > 0:
            date = file.read(Mess_Buffer)
            new_sock.send(date)
            size -= Mess_Buffer
        file.close()

    def savefile(self, new_sock, addr, tup):
      '''if user want to send a file to me, i must save it'''
      try:
        self.checkfile(tup)
        file = open("./From/"+tup[0]+"/"+tup[1]+"/"+tup[2], "wb")
        print("i have a dream , is can save a file")
        new_sock.send('Ok'.encode())
        while 1:
            date = new_sock.recv(Mess_Buffer)
            file.write(date)
      except Exception as e:
        print(e)
        file.close()
      else:
        file.close()

    def talk_to(self, *arg):
      '''before do any thing, Let's see what it is'''
      self.sock.listen(20)
      try:
        while 1:
            new_sock, addr = self.sock.accept()
            s_str = new_sock.recv(Mess_Buffer)
            s_list = Spilt_Mess.File_spilt(s_str)
            if s_str.decode().startswith('Get'):
                self.sendfile(new_sock, addr, s_list)
            else:
                self.savefile(new_sock, addr, s_list)
            new_sock.close()
      except Exception as e:
          print(e)
          new_sock.close()
