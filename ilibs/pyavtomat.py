#>>floor python-3-11-4
def contains(char,interval):
    if char>=interval[0] and char<=interval[1]:
        return 0
    elif char<interval[0]:
        return -1
    elif char>interval[1]:
        return +1
class LR0Avtomat:
    def __init__(self):
        #[(li,ri,id or del)]
        self.terminal=[]
        self.noterminal=[]
        self.stack=[]
        self.state=0
        self.top_char='S'
        self.top_type=True
        self.index=0
    def is_empty(self):
        return False
        if self.terminal==[] or self.noterminal==[]:
            return True
    def is_end_state(self,num=0):
        if len(self.noterminal[num])==1 and self.noterminal[num][0][2]<0:
            return True
        return False
    def next_state(self):
        pos=self.find(self.state,self.top_char,self.top_type)
        if pos==-1:
            return False
        else:
            if self.top_type:
                self.state=self.noterminal[self.state][pos][2]
                return True
            else:
                self.state=self.terminal[self.state][pos][2]
                return True
    def shift(self,char):
        self.top_char=char
        self.top_type=False
        self.stack.append((self.state,self.top_char,self.top_type))
        self.index+=1
        return self.next_state()
    def get_product(self):
        return self.noterminal[self.state][0][1]
    def get_decs(self):
        return self.noterminal[self.state][0][2]
    def reduce(self,dec,product):
        self.top_char=product
        self.top_type=True
        for _ in range(-dec): self.stack.pop()
        if len(self.stack)==0:  
            self.state=0
            self.stack.append((self.state,self.top_char,self.top_type))
            return self.next_state()
        else:
            self.state=self.stack[-1][0]
            self.stack.append((self.state,self.top_char,self.top_type))
            return self.next_state()
        return True
    def check(self,text):
        if self.is_empty() or len(text)==0:
            return False
        self.stack=[]#(state,terminal,type)
        self.state=0
        self.index=0
        self.shift(text[self.index])
        while True:
            if self.is_end_state(self.state):
                if not self.reduce(self.get_decs(),self.get_product()):
                    return False
            else:
                if self.index==len(text):
                    return False
                if not self.shift(text[self.index]):
                    return False
            if len(text)==self.index and len(self.stack)==1:
                break
                
        return True
            
    def find(self,state=0,char='x',flag=False):
        pos=0
        if not flag:
            lnt=len(self.terminal[state])
            pos=lnt//2
            while True:
                lnt=lnt//2
                dx=contains(char,self.terminal[state][pos])
                if dx==0:
                    return pos
                elif dx==-1:
                    pos=pos-lnt
                elif dx==+1:
                    pos=pos+lnt
                if lnt==0:
                    break
            return -1
        else:
            lnt=len(self.noterminal[state])
            pos=lnt//2
            while True:
                lnt=lnt//2
                dx=contains(char,self.noterminal[state][pos])
                if dx==0:
                    return pos
                elif dx==-1:
                    pos=pos-lnt
                elif dx==+1:
                    pos=pos+lnt
                if lnt==0:
                    break
            return -1    

    
