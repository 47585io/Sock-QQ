from copy import deepcopy
from genericpath import isfile
import multiprocessing as mut
import os
from Pubilc.Split import Spilt_Mess
Date_dir="./From/"

class users:
    '''have all date for all process'''

    def __init__(self):
        self.users = mut.Queue()
        self.users.put({})
        #olny have  a dict, {name:(addr,port)}  #save all user, and their addr,port tup
        self.friend_list = mut.Queue()
        self.friend_list.put({})
        #olny hava a dict, {groupname[friendname]}  #save group name , and he has friend name list, also save group name and it all user
        self.now_in = mut.Queue()
        self.now_in.put([])
        #olny have a list, [name] #save now_in user
        self.cache = mut.Queue()
        self.cache.put({})
        #olny hava a dict, {name:[cachemess]} #sava can't send str, wait that user login, send all to
        self.group = mut.Queue()
        self.group.put([])
        #olny hava a list, [groupname] #save all group name
         
        self.refuall()
        print(self.getto(self.friend_list),self.getto(self.cache),self.getto(self.group))
        
    def search(self, going_search_queue, new_tup):
        '''going to old going_search_queue pointer's obj search to new_tup''' 
        tmp = going_search_queue.get()
        if type(tmp) == list:
            tmp.append(new_tup)
            going_search_queue.put(tmp)
        else:
            tmp[new_tup[0]] = new_tup[1]
            going_search_queue.put(tmp)

    def getto(self, going_get_queue, index=None):
      try:
        '''get queue's dict or list index element'''
        tmp = going_get_queue.get()
        going_get_queue.put(tmp)
        if index:      
            return tmp[index]
        return tmp
      except Exception:
          return

    def add(self, tup):
        '''when a new user, call it'''
        self.search(self.users, tup)
        print("self.users:   ",self.users,tup)
        #self.search(self.friend_list, (tup[0], []))
        self.search(self.now_in, tup[0])
        print("cache:   ",self.getto(self.cache))
        self.search(self.cache, (tup[0], []))
        tmo = self.now_in.get()
        self.now_in.put(tmo)
        print("now_in  ",tmo)

    def get_friend_list(self):
        '''return user input's search after mess'''
        tmp = self.getto(self.users)
        tmp2 = self.getto(self.group)
        return str(tmp.keys())+"+"+str(tmp2)

    def Login(self, tup):
        '''when user login, call it'''
        name = tup[0].decode()
        name = name[6::]
        if name == '':
            return ''
        cache=self.getto(self.cache, name)
        self.add((name, tup[1]))
        #friend = self.getto(self.friend_list, name)
        return name+'@'+str(cache)
      
    def value_to_key(self, tmp):
        #print(self.getto(self.users)
        for key, value in self.getto(self.users).items():
            if tmp == value:
                return key

    def addgroupfriend(self, fromwho,tup):
        '''from who? who want to addfriend, then, if want add a group, must add it to group friend_list'''
        group=self.getto(self.group)
        friend_list=self.getto(self.friend_list,)
        name_list=[]
#find user want add all group name
        for name in tup:
            if name in group:
                name_list.append(name)
#all group add a friend
        for name in name_list:
            if name not in friend_list:
                friend_list[name]=[]
            friend_list[name].append(fromwho)
        self.friend_list.get()
        self.friend_list.put(friend_list)
        #self.saveall()
        
    def saveall(self):
        '''every once,save the value and not Revise the date'''
        date = self.getto(self.friend_list)
        Spilt_Mess.save_dict(Date_dir+"group_list",deepcopy(date))
          
        date2 = self.getto(self.cache)
        Spilt_Mess.save_dict(Date_dir+"mess_cache",deepcopy(date2))
        
        date3 = self.getto(self.group)
        Spilt_Mess.save_list(Date_dir+"groups",deepcopy(date3))
    
    def refuall(self):
        '''anytime, refu any date from fule'''
        redict=Spilt_Mess.refu_dict(Date_dir+"group_list",)
        for key,value in redict.items():
            self.search(self.friend_list,(key,value))
        
        redict2=Spilt_Mess.refu_dict(Date_dir+"mess_cache",)       
        for key,value in redict2.items():
            self.search(self.cache,(key,value))
        
        relist=Spilt_Mess.refu_list(Date_dir+"groups")
        for l in relist:
            self.search(self.group,l)
    
    def Isin(self,s_str,toname,fromaddr):
        '''the send to user whether in now_in?, what do i do?'''
        if toname not in self.getto(self.users):
            return 0
        if toname not in self.getto(self.now_in):
            lis=self.getto(self.cache,toname)
            if type(fromaddr)==str:
                lis.append(fromaddr+"@"+s_str)
            else:
                lis.append(self.value_to_key(fromaddr)+"@"+s_str)
            self.search(self.cache,(toname,lis))
            return 0
        return 1
    
    def exit(self,addr):
        name=self.value_to_key(addr)
        lis=self.now_in.get()
        index=lis.index(name)
        del lis[index]
        self.now_in.put(lis)
        print("已与",name,"断开连接")