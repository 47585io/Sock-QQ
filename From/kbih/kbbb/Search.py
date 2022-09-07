'''
the moudle is a easy search_appliction
you can use main() run with it
and, I have a History_Search class
'''

from copy import copy, deepcopy
from time import sleep
import tkinter as tk
import pylru
import re
from concurrent.futures import ThreadPoolExecutor
import os
import tkinter.filedialog 


class file_index:     
    def __init__(self) -> None:
        self.filename=[]
        self.indexlist=[]   
  
         
class SearchEnabelBase:
    def __init__(self) -> None:
        pass
    def text_to_words(self,text):
        pass
    def add_files(self,files):
        for file in files:
            going_to_file=open(file,"r") 
            text = going_to_file.read()
            self.proess_words_lib(file,text)
            going_to_file.close()
    def proess_words_lib(self,id,text):
        #创建words库
        pass
    def search(self,s_str):
        pass


class Update_Search(SearchEnabelBase):   
    def __init__(self) -> None:
        super(SearchEnabelBase,self).__init__()
        self.Invarted_index={}
        self.file_index={}
        
    def text_to_words(self, text):
        text=re.sub(r'[^\w]',' ',text)
        text=text.lower()
        word_list=text.split(' ')
        word_list=filter(None,word_list)
        return set(word_list)
    
    def proess_words_lib(self, id, text):       
        text=text.lower()
        char_list = list(set([s for s in text if not s.isalnum()]))
        start=0
        end=0
        word=""
        while end < len(text):
            if text[end] == ' ' or end == len(text)-1 or text[end] in char_list:
                if end == len(text)-1:
                    end += 1
                word=text[start:end]
                if word!=' ' and word!=',' and word!=None:
                    if word not in self.file_index:
                        self.file_index[word]={id:[]}
                    if id not in self.file_index[word]:
                        self.file_index[word][id]=[]
                    
                    self.file_index[word][id].append([start,end])
                start=end+1
            end+=1   
        words=self.text_to_words(text)
        for word in words:
            if word not in self.Invarted_index:
                self.Invarted_index[word]=[]
            self.Invarted_index[word].append(id)
            
    def search(self, s_str):
        check_words=list(self.text_to_words(s_str))
        check_words_goto_id_indexs=[]         
        for word in check_words:
            if word not in self.Invarted_index:
                return []
        for word in check_words:
            check_words_goto_id_indexs.append(0)
        for word in check_words:
            self.Invarted_index[word].sort()
            
        result = {}       
        while True:
            current_end_word_ids=[]
            for idx,word in enumerate(check_words):
                current_index = check_words_goto_id_indexs[idx]
                current_word_id = self.Invarted_index[word]
                if current_index >= len(current_word_id):
                    return result
                current_end_word_ids.append(current_word_id[current_index])
            if all(x==current_end_word_ids[0] for x in current_end_word_ids):
                #result.append(current_end_word_ids[0])
                result[current_end_word_ids[0]]={}
                for word in check_words:                     
                    result[current_end_word_ids[0]][word]=self.file_index[word][current_end_word_ids[0]]
                check_words_goto_id_indexs=[x+1 for x in check_words_goto_id_indexs]
                continue
            min_val=min(current_end_word_ids)
            min_index=current_end_word_ids.index(min_val)
            check_words_goto_id_indexs[min_index]+=1

    @staticmethod
    def reverser(dict):
        word_dicts = dict.values()
        word_files = dict.keys()
        result = file_index()
        result.filename = word_files
        for words in word_dicts:
            #any once,put a file_words_list from one
            end_index = []
            for word in words:
                #any once,put a word in words
                end_index.append(words[word])
            result.indexlist.append(end_index)
        return result

    @staticmethod
    def chu(file):
        lis = []
        for words in file:
            for word in words:
                lis.append(word)
        return lis


class Buffer_Search(Update_Search):
    def __init__(self,size=24) -> None:
        Update_Search.__init__(self)
        self.cache_buffer=pylru.lrucache(size)
        self.cache_buffer._lrucache__max_cache_size=24
        
    def search(self, s_str):
        if s_str in self.cache_buffer:
            return self.cache_buffer[s_str]
        result=Update_Search.search(self,s_str)
        self.cache_buffer[s_str]=result
        return result


class Graphics_Search(Buffer_Search):        
    def __init__(self,max=3) -> None:
        Buffer_Search.__init__(self) 
        self.slinepool = ThreadPoolExecutor(max)
        self.text={}  
#filename → text
        self.sult={}
#filename → now the file's word's index list
        
    def proess_words_lib(self, id, text):
        self.text[id]=text
        Update_Search.proess_words_lib(self,id,text)
           
    def quickconfig(self,win):
        win.geometry("300x55")  
        win.title("Searcher") 
        win.resizable(0,0)  
        self.farme = tk.Frame()
        self.farme.place(x=220, y=0)
        self.farme2 = tk.Frame(width=220)
        self.farme2.place(x=0, y=0)
        self.scro=tk.Scrollbar(win,orient=tk.HORIZONTAL)        
        self.ent=tk.Entry(self.farme2, selectbackground='blue',xscrollcommand=self.scro.set,width=18)
        self.ent.pack(side='left',fill=tk.Y)
        self.scro.config(command=self.ent.xview)
        self.scro.pack(fill=tk.X,side="bottom")
        self.but = tk.Button(self.farme, text="search",command=self.search_with)
        self.but.pack()
        
    @staticmethod    
    def open_text(val,s_str,l_list):
        wintext = tk.Tk()
        wintext.title(val)
        #win.resizable(0,0)  
        xscro = tk.Scrollbar(wintext, orient=tk.HORIZONTAL)
        yscro = tk.Scrollbar(wintext)
        xscro.pack(side='bottom',fill=tk.X)
        yscro.pack(side='right',fill=tk.Y)
        text = tk.Text(wintext,width=55,height=15,xscrollcommand=xscro.set,yscrollcommand=yscro.set)
        xscro.config(command=text.xview)
        yscro.config(command=text.yview)
        text.insert("end", s_str)
        text.pack()
        
        def index_to_str(text,list):
            row=1
            #the small line is 1
            col=-1
            #any line start index from 0,and not have start index,and have end index
            index=0
            while index<=list:
                if text[index-1]=='\n' and index!=0:
                    row+=1
                    col=-1
                col+=1
                index+=1
            return str(row)+"."+str(col)
        
        for l in l_list:
            text.tag_add(str(l[0]),index_to_str(s_str,l[0]),index_to_str(s_str,l[1]))
            text.tag_config(str(l[0]),foreground='red')  
        wintext.update()

    def open_file(self, comlist):
        val=""
        try:
            val=comlist.get(comlist.curselection())
        except Exception as e:
            return
        self.open_text(val,self.text[val],self.sult[val])
    
    def showlist(self,comlist,result):  
        new_result=self.reverser(result)         
        j=0
       # name_list=[]
        comlist.delete(0,"end")
        for i in new_result.filename:           
            comlist.insert("end",i)
            self.sult[i]=self.chu(new_result.indexlist[j])
            j+=1
        
    def search_with_but(self):
        listwin = tk.Tk()
        listwin.title("查找结果")
        listwin.resizable(0, 0)
        tmp=""
        yscro=tk.Scrollbar(listwin)
        yscro.pack(side='right',fill=tk.Y)
        xscro=tk.Scrollbar(listwin,orient=tk.HORIZONTAL)
        xscro.pack(side='bottom',fill=tk.X)
        comlist = tk.Listbox(listwin,height=300,xscrollcommand=xscro.set, yscrollcommand=yscro.set,selectbackground='pink')
        but = tk.Button(listwin, text='打开文件',command= lambda :self.open_file(comlist))
        but.pack(side='top')
        comlist.pack()
        yscro.config(command=comlist.yview)
        xscro.config(command=comlist.xview)
        listwin.geometry("300x300")    
        while 1:
          try:
            if not self.ent.get():
                tmp=""
                comlist.delete(0, "end")
            elif tmp == self.ent.get() :
                pass
            else:
                result = Buffer_Search.search(self,self.ent.get())
                if not result:
                    tmp = self.ent.get()
                    comlist.delete(0,"end")                   
                else: 
                    tmp = self.ent.get()
                    self.showlist(comlist,result)
                    #防止in 0.1s time  and it get input
          except Exception as e:              
                pass    
          listwin.update()            
        listwin.mainloop()     
          
    def search_with(self):
        self.slinepool.submit(self.search_with_but)
    

class History_Search(Graphics_Search):
    count=0
    def __init__(self,max=3):
        Graphics_Search.__init__(self,max)
        self.index={}
        #the key is index,val is filename text
        self.rust={}
        #the key is index,val is sult
        
    def key_to_file(self,val,count):
        self.open_text(val,self.index[str(count)],self.rust[str(count)])
        
    def open_file(self, comlist):
        val = ""
        try:
            val = comlist.get(comlist.curselection())
        except Exception as e:
            return
        count=self.count
        self.index[str(count)] =self.text[val]
        self.rust[str(count)] = deepcopy(self.sult[val])
        self.menu_son.add_command(label=val,command=lambda:self.key_to_file(val,count))
        self.count+=1
        self.open_text(val,self.text[val], self.sult[val])
    
    def pos(self,enxy):
        self.menu.post(enxy.x_root,enxy.y_root+30)
        
    def after_add_files(self):
        file_tuple=tkinter.filedialog.askopenfilenames(title='file picker',initialdir='../')
        if file_tuple=="":
            return
        else:
            self.add_files(file_tuple)
    
    def quickconfig(self, win):
        Graphics_Search.quickconfig(self,win)
        self.menu=tk.Menu(win,tearoff=False,activebackground="pink")
        self.menu_son=tk.Menu(self.menu,tearoff=False,activebackground="pink")
        self.menu_son2=tk.Menu(self.menu,activebackground='pink',tearoff=False)
        self.menu.add_cascade(label="查看历史记录",menu=self.menu_son)
        self.menu.add_command(label="add file",command=self.after_add_files)
        win.bind("<Button-3>", self.pos)
        
    ''' def show(self,i):
        while True:
            self.open()
            if xxz:
                show(i+1)
            elif xxx:
                return
            elif xcc:
                exit()
            '''
     
                          
def main(): 
    my_search = History_Search()
    #my_search.add_files(["1.txt","2.txt","3.txt","/home/tom/vscode/HTML/1.html"])
    win=tk.Tk()
    my_search.quickconfig(win)
    win.mainloop()

if __name__=='__main__':    
    main()
    