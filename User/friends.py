from Pubilc.Split import Spilt_Mess
from User.UDPmess import UDP,UDP_SOCK

class friends:
    '''The all friend date save in'''

    def __init__(self) -> None:
        self.friend_list = []
        # friend name list
        self.pic = []
        #friend 头像
        self.talk_with = ""
        # who talk with now
        self.tmp = []
        # 存储临时抓 friend list

    def show(self):
        return self.friend_list

    def format_list(self, list_):
        '''format the going to add list'''
        if type(list_) == str:
            if list_ not in self.friend_list:
                return [list_,]
            return
        new_list = []
        for name in list_:
            if name not in self.friend_list and name not in new_list and name not in self.tmp:
                new_list.append(name)
        return new_list

    def __from_server_get_friend_list(self, mess, sock):
        '''func name is i mean'''
        mess.Send(sock, "AddFriend ")
        s_str = mess.getSpecial()
        return Spilt_Mess.Friend_list_Read_Spilt(s_str)

    def addfriend(self, mess=UDP, sock=UDP_SOCK):
        '''get friend list and show'''
        list_ = self.__from_server_get_friend_list(mess, sock)
        list_ = self.format_list(list_)
        self.tmp.extend(list_)

    def Search_Friend(self, name_str):
        '''search name_str in friend_list'''
        if not name_str:
            #print("no name")
            return
        name_list = []
        for i in self.tmp:
            if i.find(name_str) != -1:
                name_list.append(i)
        return name_list


Friend_List = friends()
# sava all friend


