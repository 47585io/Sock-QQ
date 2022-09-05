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
        self.group.put(['one'])
        #olny hava a list, [groupname] #save all group name
         
        if os.path.isfile(Date_dir+"group_list"):
            file = open(Date_dir+"group_list", "r")
            lis=file.readlines()
            for g in lis:
                tup=Spilt_Mess.Refu_Date_Spilt(g)
                self.search(self.friend_list,tup)
            file.close()
         
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
        '''get queue's dict or list index element'''
        tmp = going_get_queue.get()
        going_get_queue.put(tmp)
        if index:
            return tmp[index]
        return tmp

    def add(self, tup):
        '''when a new user, call it'''
        self.search(self.users, tup)
        self.search(self.friend_list, (tup[0], []))
        self.search(self.now_in, tup[0])
        self.search(self.cache, (tup[0], []))
        tmo = self.now_in.get()
        self.now_in.put(tmo)
        print(tmo)

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
        self.add((name, tup[1]))
        friend = self.getto(self.friend_list, name)
        return name+str(friend)

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
        self.saveall()
        
    def saveall(self):
        date=self.friend_list.get()
        file=open(Date_dir+"group_list","w")
        for groupname, name in date.items():
            file.write(groupname+"###"+str(name)+'\n')
        file.close()
