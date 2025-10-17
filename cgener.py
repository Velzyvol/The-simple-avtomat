#>>floor python-3-11-4

from LRParsing import *
from Symbols import *
from intervalast import intervalast

def maketabs(count):
    res=""
    for i in range(count):
        res+='\t'
    return res
def inputtabs(count,text):
    lines=text.splitlines()
    tabs=maketabs(count)
    for i in range(len(lines)):
        lines[i]=tabs+lines[i]
    res=""
    for i in range(len(lines)):
        res+=lines[i]+'\n'
    return res    
#Тут возврощаем код питона после исполнения препроцессором
def mashin_on_python_tableparse(mashin):
    #{(flag,term):stateid}
    code=""
    for i in range(len(mashin.States)):
        code+="state_terminal"+i.__str__()+"=["
        iast=intervalast()
        iast.convert_from(mashin.States[i])
        print(iast.__str__())
        for j in range(len(iast.terminal)):
            print(j)
            if j!=len(iast.terminal)-1:
                code+=iast.terminal[j].__str__()+","
            else:
                code+=iast.terminal[j].__str__()
                
        code+="]\n"
        code+="state_noterminal"+i.__str__()+"=["
        for j in range(len(iast.noterminal)):
            print(j)
            if j!=len(iast.noterminal)-1:
                code+=iast.noterminal[j].__str__()+","
            else:
                code+=iast.noterminal[j].__str__()
        code+="]\n"


        
    code+="avtomat_states=["
    for i in range(len(mashin.States)):
        if i!=len(mashin.States)-1:
            code+="(state_terminal"+i.__str__()+",state_noterminal"+i.__str__()+"),"
        else:
            code+="(state_terminal"+i.__str__()+",state_noterminal"+i.__str__()+")"
    code+="]\n"    
    return code



jmp=dict()

sit=LRSituation()
sit.add(rule('S:.xy'))
sit.add(rule('S:.`S`S'))


mash=LRMashin(sit)

for i in range(len(mash.States)):
    print(mash.States[i].Situation)


print(mashin_on_python_tableparse(mash))





