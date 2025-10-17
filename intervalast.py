import Symbols

#true-меньше false-больше
def compareS(a,b):
    if(ord(a[1])<ord(b[0])):
        return True
    elif (ord(a[0])>ord(b[1])):
        return False
def contains(char,interval):
    if char>=interval[0] and char<=interval[1]:
        return 0
    elif char<interval[0]:
        return -1
    elif char>interval[1]:
        return +1
class intervalast:
    #terminal=[(char,char,object)]
    #noterminal=[(char,char,object)]
    def __init__(self):
        self.terminal=[]
        self.noterminal=[]
    def sort_terminal(self):
        for i in range(len(self.terminal)):
            for j in range(len(self.terminal)-i):
                if compareS(self.terminal[i],self.terminal[j]):
                    old=self.terminal[i]
                    self.terminal[i]=self.terminal[j]
                    self.terminal[j]=old
                    break
    def sort_noterminal(self):
        for i in range(len(self.noterminal)):
            for j in range(len(self.noterminal)-i):
                if compareS(self.noterminal[i],self.noterminal[j]):
                    old=self.noterminal[i]
                    self.noterminal[i]=self.noterminal[j]
                    self.noterminal[j]=old
                    break
    def sort(self):
        self.sort_terminal()
        self.sort_noterminal()
    def find(self,char='x',flag=False):
        pos=0
        if flag:
            lnt=len(self.terminal)
            pos=lnt//2
            while lnt!=0:
                lnt=lnt//2
                dx=contains(char,self.terminal[pos])
                if dx==0:
                    return self.terminal[pos]
                elif dx==-1:
                    pos=pos-lnt
                elif dx==+1:
                    pos=pos+lnt
            return None
        else:
            lnt=len(self.noterminal)
            pos=lnt//2
            while lnt!=0:
                lnt=lnt//2
                dx=contains(char,self.noterminal[pos])
                if dx==0:
                    return self.noterminal[pos]
                elif dx==-1:
                    pos=pos-lnt
                elif dx==+1:
                    pos=pos+lnt
            return None
    def __str__(self): 
        res='noterminal:'+len(self.noterminal).__str__()+'\n'+'terminal:'+len(self.terminal).__str__()+'\n'
        for i in range(len(self.terminal)):
            res=res+self.terminal[i].__str__()+' '
        for i in range(len(self.noterminal)):
            res=res+self.noterminal[i].__str__()+' '
        return res+'\n'
    def convert_from(self,state):
        asslist=state.Direct
        if len(state.Direct.Item)==0:
            product=chr(state.Situation.Rules[0].Product.Value)
            decr=len(state.Situation.Rules[0].Stages);
            self.noterminal.append((product,product,-decr))
            return
        for i in range(len(asslist.Item)):
            if not asslist.Item[i].Key.Left.Terminal:
                self.terminal.append(
                    (chr(asslist.Item[i].Key.Left.Value),
                     chr(asslist.Item[i].Key.Right.Value),
                     asslist.Item[i].Value.id))
            else:
                 self.noterminal.append(
                    (chr(asslist.Item[i].Key.Left.Value),
                     chr(asslist.Item[i].Key.Right.Value),
                     asslist.Item[i].Value.id))   

