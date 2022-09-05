from ossaudiodev import SNDCTL_DSP_SETFRAGMENT


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
    def put_a_var(self):
        pass
    
    def del_a_var(self):
        pass
    
    def saveall(self):
        pass
    
    def refuall(self):
        pass
    
    def put_a_mess(self,who,s_str):
        if who not in self.Mess_Friend:
            self.Mess_Friend[who]=[]
        self.Mess_Friend[who].append(s_str)
    
    def put_a_file(self):
        pass
    
    def get_a_file(self):
        pass
    
    