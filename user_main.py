import atexit
from User.UDPmess import UDP_SOCK,UDP
from User.TCPmess import TCP_SOCK,TCP
from User.friends import Friend_List
from User.Talk_with import Talk_with

def whenexit():
    '''when exit, close all sock'''
    UDP.Send(UDP_SOCK,"EXIT")
    UDP_SOCK.close()
    TCP_SOCK.close()
atexit.register(whenexit)

GNU = Talk_with()
def main(mess, sock,tcpmess, tcpsock, friends, gra):
    gra.quickconfig(friends, mess, sock,tcpmess,tcpsock)
    gra.run()


main(UDP,UDP_SOCK, TCP,TCP_SOCK, Friend_List, GNU)
