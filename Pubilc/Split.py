import os

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
                while True:
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
        file = os.path.basename(filename)
        return ("Send√From√" + fromwho + "√To√" + to + "√" + file + "√and√" + size).encode()

    @staticmethod
    def Get_mess_spilt(fromwho, to, filename):
        file=os.path.basename(filename)
        return ("Get√From√" + fromwho + "√To√" + to + "√" + file + "√and√" + "no").encode()

    @staticmethod
    def File_spilt(s_str):
        #From who to who filename and size
        s_str = s_str.decode()
        lis = s_str.split("√", 7)
        return (lis[2], lis[4], lis[5],lis[7])
