
import os
from Pubilc.Split import Spilt_Mess
import sys
from User.TCPmess import MY_DIR

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
        self.mydir = "./mydir/"
        self.friend_file=self.mydir+"friend"
    #friens name and pic
        self.mess_file=self.mydir+"mess"
    #friends mess
        self.file_get=self.mydir+"get"
       
    def start_var(self):
        self.var_file=self.mydir+"var"
        self.var_obj=open(self.var_file,"w")     
        self.stdout=sys.stdout
        self.stderr=sys.stderr
        sys.stdout=self.var_file
        sys.stderr=self.var_file
    
    def end_var(self):
        sys.stdout = self.stdout
        sys.stderr=self.stderr
        self.var_obj.close()
    
    def savedict(self,file,dict):
        for name,mess in dict.items():
            file.write(str(name)+"###"+str(mess)+'\n')
    
    def savetwo(self,file,dict,):
        '''save a two with file'''
        i=0
        while i<len(dict[1]):
            file.write(str(dict[0][i])+"###"+str(dict[1][i])+'\n')
            i+=1
        file.close()
    
    def saveall(self,friends):
        file=open(self.friend_file,"w")
        file2=open(self.mess_file,"w")
        file3 = open(self.file_get, "w")
        try:
            self.savetwo(file,(friends.friend_list,friends.pic))
            self.savedict(file2,self.Mess_Friend)
        except Exception as e:
            print(e)
        try:
            for name,mess in self.File_all.items():
                self.File_all[name] = [get.decode() for get in mess]
        except Exception as e:
            print(e)
            print(self.File_all)
        self.savedict(file3, self.File_all)
        file.close()
        file2.close()
        file3.close()
        print("save finish")
        
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
        if os.path.isfile(self.file_get):
            file3 = open(self.file_get, "r")
            lines=file3.readlines()
            for line in lines:
                self.refu_a_dict(line,self.File_all)
            file3.close()
            for name in self.File_all.keys():
                self.File_all[name] = [ get.encode() for get in self.File_all[name]]
    
    def put_a_mess(self,who,s_str):
        if who not in self.Mess_Friend:
            self.Mess_Friend[who]=[]
        self.Mess_Friend[who].append(s_str)
        if len(self.Mess_Friend[who])>self.maxmess:
            del self.Mess_Friend[who][0]
            self.maxmess-=1
    
    