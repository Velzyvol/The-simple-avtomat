
class Symbol:
    def __init__(self,Value=0,Terminal=False):
        self.Value=Value
        self.Terminal=Terminal
    def __str__(self):
        if(self.Terminal):
            return '`'+chr(self.Value)
        else:
            return chr(self.Value)
    def Clone(self):
        return Symbol(self.Value,self.Terminal)
    def __eq__(self,val):
        return (self.Value==val.Value)and(self.Terminal==val.Terminal)
    def __ne__(self,val):
        return not((self.Value==val.Value)and(self.Terminal==val.Terminal))
class SymbolInterval:
    def __init__(self,Left=Symbol(1,False),Right=Symbol(-1,False)):
        self.Left=Left.Clone()
        self.Right=Right.Clone()
    def isEmpty(self):
        return self.Left.Value>self.Right.Value
    def Contains(self,smbl=None):
        if self.isEmpty():
            return False
        elif self.Left.Terminal==smbl.Terminal:
            if(self.Left.Value<=smbl.Value)and(self.Right.Value>=smbl.Value):
                return True
            else:
                return False
    def Intersect(self,intr=None):
        if intr.isEmpty() or self.isEmpty():
            return False
        else:
            if(self.Contains(intr.Left))or(self.Contains(intr.Right)or(intr.Contains(self.Left))or(intr.Contains(self.Right))):
                return True
            else:
                return False
    def leftClip(self,intr=None):
        if(self.Contains(intr.Left)):
            sintr=SymbolInterval(self.Left,intr.Left)
            sintr.Right.Value-=1
        else:
            sintr=SymbolInterval()
        return sintr
    def rightClip(self,intr=None):
        if(self.Contains(intr.Right)):
            sintr=SymbolInterval(intr.Right,self.Right)
            sintr.Left.Value+=1
        else:
            sintr=SymbolInterval()
        return sintr
    def isInput(self,intr):
        if(self.Contains(intr.Left))and(self.Contains(intr.Right)):
            return True
        else:
            return False
    def __str__(self):
        if(not self.isEmpty()):
            return '['+self.Left.__str__()+','+self.Right.__str__()+']'
        else:
            return '[]'
    def __eq__(self,val):
        if self.isEmpty() and val.isEmpty():
            return True
        else:
            return self.Left==val.Left and self.Right==val.Right
            
    def Clone(self):
        return SymbolInterval(self.Left,self.Right)
class SymbolAssocListNode:
    def __init__(self,Key=None,Value=None):
        self.Key=Key.Clone()
        self.Value=Value
    def __str__(self):
        return self.Key.__str__()+'->'+self.Value.__str__()
    
class SymbolAssocList:
    def __init__(self):
        self.Item=list()
    def get_intersect(self,key=None):
        res=list()
        for i in range(len(self.Item)):
            if(self.Item[i].Key.Intersect(key)):
                res.append(i)
        return res
    def Input(self,key=None,value=None):
        if type(key) is Symbol:
            oldkey=key
            key=SymbolInterval(oldkey,oldkey)
            
        itrlist=self.get_intersect(key)
        if(len(itrlist)==0):
            self.Item.append(SymbolAssocListNode(key,value))
        elif(len(itrlist)==1)and(len(self.Item)==1):
            if(self.Item[0].Key.isInput(key)):
                self.Item[0]=SymbolAssocListNode(key,value)
            elif(key.Intersect(self.Item[0].Key)):
                lClip=self.Item[0].Key.leftClip(key)
                rClip=self.Item[0].Key.rightClip(key)
                old=self.Item[0].Value
                self.Item=[SymbolAssocListNode(key,value)]
                if(not lClip.isEmpty()):
                    self.Item.append(SymbolAssocListNode(lClip,old))
                if(not rClip.isEmpty()):
                    self.Item.append(SymbolAssocListNode(rClip,old))
        elif(len(itrlist)>=1):
            deli=0
            for i in itrlist:
                lClip=self.Item[i-deli].Key.leftClip(key)
                rClip=self.Item[i-deli].Key.rightClip(key)
                lempty=lClip.isEmpty()
                rempty=rClip.isEmpty()
                if(lempty)and(rempty):
                    self.Item.pop(i-deli)
                    deli+=1
                elif(not lempty)and(rempty):
                    self.Item[i-deli]=SymbolAssocListNode(lClip,self.Item[i-deli].Value)
                elif(lempty)and(not rempty):
                    self.Item[i-deli]=SymbolAssocListNode(rClip,self.Item[i-deli].Value)
            self.Item.append(SymbolAssocListNode(key,value))
    def Find(self,key):
        for elm in self.Item:
            if(elm.Key.Contains(key)):
                return elm.Value
        return None
                
    def __str__(self):
        res=''
        for elm in self.Item:
            res+=elm.__str__()+'   '
        return res

def symbol(value=0,terminal=False):
    if(type(value) is int):
        res=Symbol(value,terminal)
    elif(type(value) is str):
        res=Symbol(ord(value),terminal)
    return res

def interval(left=0,right=0,terminal=False):
    if(type(left) is int):
        s1=Symbol(left,terminal)
    elif(type(left) is str):
        s1=Symbol(ord(left),terminal)
    if(type(right) is int):
        s2=Symbol(right,terminal)
    elif(type(right) is str): 
        s2=Symbol(ord(right),terminal)
    sintr=SymbolInterval(s1,s2)
    return sintr


