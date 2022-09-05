from ossaudiodev import SNDCTL_DSP_SETFRAGMENT
import os
from Pubilc.Split import Spilt_Mess

class History:
    def __init__(self) -> None:
        self.Mess_Friend = {}
 # 记录与好友通信完全mess
        self.File_all={}
 # save file
        self.var=""
 #日志
        self.maxmess=100
 #mess最多保存count
        self.friend_file="./friend"
    #friens name and pic
        self.mess_file="./mess"
    #friends mess
       
    def put_a_var(self):
        pass
    
    def del_a_var(self):
        pass
    
    def savedict(self,file,dict):
        for name,mess in dict.items():
            file.write(str(name)+"###"+str(mess)+'\n')
        pass
    
    def savetwo(self,file,dict,):
        '''save a two with file'''
        i=0
        while i<len(dict):
            file.write(str(dict[0][i])+"###"+str(dict[1][i])+'\n')
            i+=1
        file.close()
    
    def saveall(self,friends):
        print("save")
        file=open(self.friend_file,"w")
        file2=open(self.mess_file,"w")
        self.savetwo(file,(friends.friend_list,friends.pic))
        self.savedict(file2,self.Mess_Friend)
        file.close()
        file2.close()
        
    def refu_a_two(self,s,tup):
        index = s.find("###")
        tup[0] .append(s[0:index:])
        tup[1] .append(s[index+3:-1:])
    
    def refu_a_dict(self,dic_s,dict):
        index=dic_s.find("###")
        name = dic_s[0:index:]
        dict[name]=[]
        index+=3
        mess_str=dic_s[index:-1:]
        lis=Spilt_Mess.Friend_list_Read_Spilt(mess_str.encode())
        dict[name]=lis
    
    def refuall(self,friends):
        if os.path.isfile(self.friend_file):
            print("refu")
            file = open(self.friend_file, "r")
            lines=file.readlines()
            for line in lines:
                self.refu_a_two(line,(friends.friend_list,friends.pic))
            file.close()
        if os.path.isfile(self.mess_file):
            file2 = open(self.mess_file, "r")
            lines=file2.readlines()
            for line in lines:
                self.refu_a_dict(line,self.Mess_Friend)
            file2.close()           
    
    def put_a_mess(self,who,s_str):
        if who not in self.Mess_Friend:
            self.Mess_Friend[who]=[]
        self.Mess_Friend[who].append(s_str)
    
   
    
    def put_a_file(self):
        pass
    
    def get_a_file(self):
        pass
    
    