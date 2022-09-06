from Server.TCPmess import TCP_Mess
from Server.UDPmess import message
from Server.users import mut
import threading as th
import atexit
PRO_MAX = 1
# 设置要为每个server init's process and sline count

def start(mess, arg):
    
    for i in range(PRO_MAX):
        s = th.Thread(target=mess.talk_to, args=(arg,))
        s.setDaemon(True)
        s.start()
        
    mess.talk_to(arg)
#all sline share date on the process


def main(messes, arg):
    pro_list = []
    for mess in messes:
        pro = mut.Process(target=start, args=(mess, arg))
        pro.start()
        pro_list.append(pro)
    #start(messes[0], arg)
    input()
    for pro in pro_list:
        pro.kill()
    exit(0)

#The one process olny have a mess server, a mess server can in diffrent port or process, but their share queue
# any pro can open sline,and call talk_to, and any sline can call talk_to
# defalut,the one port olny init one
# but, you can append it's pointer many count in messes list, you can init many frequency
# like below


messes = [message(), TCP_Mess(),]
messes.append(messes[0])
# messes.append(users())


def whenexit():
    '''when exit, clo