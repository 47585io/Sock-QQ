import dataclasses
from genericpath import isdir
import os

from numpy import set_string_function

class Spilt_Mess:
    '''The class have many process mess's func'''
    @staticmethod
    def Send_spilt(s_str, name):
        '''when send a defalut mess ,use it'''
        if name:
            return (name+"@"+s_str).encode()
        else:
            return s_str.encode()

    @staticmethod
    def Read_spilt(s_str):
        '''when read a defalut mess ,use it'''
        if s_str:
            s_str = s_str.decode()
            index = s_str.find(('@'))
            read_str = s_str[index+1::]
            name = s_str[0:index:]
            return (read_str, name)

    @staticmethod
    def Friend_list_Send_Spilt(friend_list):
        '''when send a friend_list, call it'''
        s_str = ""
        for friend in friend_list:
            s_str += "'"
            s_str += friend
            s_str += "'"
        return s_str.encode()

    @staticmethod
    def Friend_list_Read_Spilt(s_str):
        '''when read a friend_list,call it'''
        s_str = s_str.decode()
        friend_list = []
        start, end, index = (0, 0, 0)
        while index < len(s_str):
            if s_str[index] == "'":
                start = index+1
                index += 1
                while index<len(s_str):
                    if s_str[index] == "'":
                        end = index
                        friend_list.append(s_str[start:end:])
                        break
                    index += 1
            index += 1
        return friend_list

    @staticmethod
    def Label_Add(s_str, num):
        return (str(num)+':'+s_str).encode()

    @staticmethod
    def Label_Del(s_str):
        s_str = s_str.decode()
        index = s_str.find(':')
        return (int(s_str[0:index:]), s_str[index+1::])

    @staticmethod
    def Send_mess_spilt(fromwho, to, filename,size):
        '''when want send a file, call it init a send to server str'''
        file = os.path.basename(filename)
        return ("Send√From√" + fromwho + "√To√" + to + "√" + file + "√and√" + size).encode()

    @staticmethod
    def Get_mess_spilt(fromwho, to, filename):
        '''when want get a file from server, call it init a get str'''
        file=os.path.basename(filename)
        return ("Get√From√" + fromwho + "√To√" + to + "√" + file + "√and√" + "no").encode()

    @staticmethod
    def File_spilt(s_str):
      '''when get a Send or Get str, Spilt it, you hava lis,[From,To,filename,(size)]'''
      #From who to who filename and size
      try:
        s_str = s_str.decode()
        lis = s_str.split("√", 7)
        return (lis[2], lis[4], lis[5],lis[7])
      except Exception:
          return 0
      
    @staticmethod
    def Sava_Self_mess(s_str):
        return "MY#"+s_str
      
    def Re_Self_mess(s_str):
        return s_str[3::]
    
    @staticmethod
    def calculate_text(text,width,size):
        line = len(text)*size//width
        addtoy= line*size
        mid=width//2
        return (addtoy,mid)
    
    @staticmethod
    def Sava_Date_Spilt(name,date):
        return str(name)+"###"+str(date)+'\n'

    @staticmethod
    def Refu_Date_Spilt(s_str):
        index = s_str.find("###")
        name = s_str[0:index:]
        index += 3
        mess_str = s_str[index:-1:]
        lis = Spilt_Mess. Friend_list_Read_Spilt(mess_str.encode())
        return (name,lis)
    
    @staticmethod
    def save_dict(filename,dict):
      try:
        print(filename,dict)
        file = open(filename,"w")
        for name,date in dict.items():
            file.write(Spilt_Mess.Sava_Date_Spilt(name,date))
        file.close()
      except Exception:
          file.close()
     
    @staticmethod
    def refu_dict(filename,):
        redict={}
        if os.path.isfile(filename):
            file = open(filename, "r")
            lis = file.readlines()
            for g in lis:
                tup = Spilt_Mess.Refu_Date_Spilt(g)
                redict[tup[0]]=tup[1]
            file.close()
            return redict
    
    @staticmethod
    def save_list(filename,list):
        print(filename,list)
        file = open(filename, "w")
        file.write(str(list))
        file.close()
    
    @staticmethod
    def refu_list(filename, ):
        relist=[]
        if os.path.isfile(filename):
            file = open(filename, "r")
            s=file.read()
            relist= Spilt_Mess.Friend_list_Read_Spilt(s.encode())
            file.close()
            return relist
