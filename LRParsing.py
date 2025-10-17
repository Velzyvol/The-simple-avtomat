#>>floor python-3-11-4

#Грамматика должна удовлетворять условиям LR(0) грамматик.

from Symbols import *

class SymbolSet:
    def __init__(self):
        self.Index=0
        self.Item=list()
    def add(self,val):
        if self.contains(val)==False:
            self.Item.append(val)
    def contains(self,val):
        for elem in self.Item:
            if (type(val) is type(elem))and(val==elem):
                return True
        return False
    def __iter__(self):
        self.Index=0
        return self
    def __next__(self):
        if self.Index<len(self.Item):
            result=self.Item[self.Index]
            self.Index+=1
            return result
        else:
            raise StopIteration
        

class LRRule:
    #product
    #stages
    #point
    def __init__(self):
        self.Product=symbol('S',True)
        self.Stages=[symbol('a')]
        self.Point=0
    def endStage(self):
        return len(self.Stages)==self.Point
    def __eq__(self,val):
        if(self.Product==val.Product)and(self.Point==val.Point)and(len(self.Stages)==len(val.Stages)):
            for i in range(len(self.Stages)):
                if(self.Stages[i]!=val.Stages[i]):
                    return False
            return True
        return False
    def __ne__(self,val):
        return not self.__eq__(self,val)
    def Clone(self):
        result=LRRule()
        result.Product=self.Product.Clone()
        result.Stages=list()
        result.Point=self.Point
        for i in range(len(self.Stages)):
            result.Stages.append(self.Stages[i].Clone())
        return result
    def __str__(self):
        result=''
        result+=self.Product.__str__()+':'
        for i in range(len(self.Stages)):
            if i==self.Point:
                result+='.'
            if i<len(self.Stages):
                result+=self.Stages[i].__str__()

        return result
    
class LRSituation:
    #Rules
    def __init__(self):
        self.Rules=[]
    def nextSet(self):
        result=SymbolSet()
        for r in self.Rules:
            result.add(r.Stages[r.Point])
        return result
    def contains(self,rul):
        for rl in self.Rules:
            if(rl==rul):
                return True
        return False
    def __eq__(self,val):
        if(len(self.Rules)==len(val.Rules)):
            for i in range(len(self.Rules)):
                if(not val.contains(self.Rules[i])):
                    return False
            return True
        return False
    def add(self,rule):
        self.Rules.append(rule)
    def __ne__(self,val):
        return self.__eq__(self,val)
    def next(self,sign):
        result=LRSituation()
        for rul in self.Rules:
            if(rul.Stages[rul.Point]==sign):
                clrul=rul.Clone()
                clrul.Point+=1
                result.Rules.append(clrul)
        return result
    def endProduct(self):
        if len(self.Rules)==1:
            if self.Rules[0].endStage():
                return True
        return False
    def __str__(self):
        result=''
        for el in self.Rules:
            result+=el.__str__()+'\n'
            
        return result
    def clone(self):
        result=LRSituation()
        for e in self.Rules:
            result.add(e.Clone())
        return result
    def final(self):
        for r in self.Rules:
            if r.endStage():
                return True
        return False
class LRState:
    def __init__(self,sid=0):
        self.Situation=LRSituation()
        self.Direct=SymbolAssocList()
        self.id=sid
class LRMashin:
    def __init__(self,grammar):
        self.States=[]
        state0=LRState(sid=0)
        state0.Situation=grammar.clone()
        self.States.append(state0)
        newStates=[]
        index=0
        while index<len(self.States):
            tstate=self.States[index]
            if not tstate.Situation.final():
                signset=tstate.Situation.nextSet()
                for sign in signset:
                    sit=tstate.Situation.next(sign)
                    fstate=self.findState(sit)
                    if fstate==None:
                        fstate=LRState(sid=len(self.States))
                        fstate.Situation=sit
                        tstate.Direct.Input(sign,fstate)
                        self.States.append(fstate)
                    else:
                        tstate.Direct.Input(sign,fstate)
            index+=1        
    def findState(self,sit):
        for s in self.States:
            if s.Situation==sit:
                return s
        return None
    def parse(string):
        pass
    def parseFile(path):
        pass

def rule(strrule):
    rul=LRRule()
    rul.product=strrule[0]
    if len(strrule)==4:
        rul.Stages.append(symbol(strrule[4]))
        rul.Point=0
    else:
        rul.point=0
        rul.Stages=[]
        flg=False
        for i in range(len(strrule)-2):
            if(strrule[i+2]=='.'):
                rul.point=len(rul.Stages)
            else:
                if(strrule[i+2]=='`'):
                    flg=True
                else:
                    rul.Stages.append(symbol(strrule[2+i],flg))
                    flg=False
    return rul



"""
pyast

sit=LRSituation()
sit.add(rule('S:.()'))
sit.add(rule('S:.(`S)'))
sit.add(rule('S:.`S`S'))

mash=LRMashin(sit)

for x in mash.States:
    print(x.Situation)

!x!y in ADD @obj f(x+'+'+y)=obj and obj.left=f(x) and obj.right=f(y)

for s,x,y in (str,name,name):
    if s==x+'+'+y:
        add=ClassAdd()
        add.left=x
        add.right=y
        f(s)=add


for x,y in ClassAdd:
    if type(x) is ClassAdd and type(y) is ClassAdd:
        obj=ClassAdd()
        obj.Left=x
        obj.Right=x
        obj.__str__()=x.__str__()+'+'+y.__str__()


for x,y in ADD:
    f(x+'+'+y)=obj
    obj.left=f(x)
    obj.right=f(y)
    obj.text=x+'+'+y
    
    degression for "N" to "M"

for x in names:
    
"""
