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
def mashin_on_python_tableparse(mashin,pref='0'):
    #{(flag,term):stateid}
    code="avtomat=LR0Avtomat()"'\n'
    for i in range(len(mashin.States)):
        code+="state_terminal"+i.__str__()+"=["
        iast=intervalast()
        iast.convert_from(mashin.States[i])
        for j in range(len(iast.terminal)):
            if j!=len(iast.terminal)-1:
                code+=iast.terminal[j].__str__()+","
            else:
                code+=iast.terminal[j].__str__()
        code+="]\n"
        code+="state_noterminal"+i.__str__()+"=["
        for j in range(len(iast.noterminal)):
            if j!=len(iast.noterminal)-1:
                code+=iast.noterminal[j].__str__()+","
            else:
                code+=iast.noterminal[j].__str__()
        code+="]\n"
    code+="avtomat.terminal=["
    for i in range(len(mashin.States)):
        if i!=len(mashin.States)-1:
            code+="state_terminal"+i.__str__()+','
        else:
            code+="state_terminal"+i.__str__()
    code+="]\n"
    code+="avtomat.noterminal=["
    for i in range(len(mashin.States)):
        if i!=len(mashin.States)-1:
            code+="state_noterminal"+i.__str__()+','
        else:
            code+="state_noterminal"+i.__str__()
    code+="]\n"
    code+="return avtomat"'\n'
    code=inputtabs(1,code)
    code="def avtomat_init_"+pref+"():"'\n'+code
    
    return code



jmp=dict()

sit=LRSituation()
sit.add(rule('E:.()'))
sit.add(rule('E:.`E`E'))
sit.add(rule('E:.(`E)'))

mash=LRMashin(sit)


for i in range(len(mash.States)):
    print(i)
    print(mash.States[i].Situation)
    

print(mashin_on_python_tableparse(mash))






