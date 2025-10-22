#>>floor python-3-11-4
from  pyavtomat import *

def avtomat_init_0():
	avtomat=LR0Avtomat()
	state_terminal0=[('(', '(', 1)]
	state_noterminal0=[('E', 'E', 2)]
	state_terminal1=[(')', ')', 3),('(', '(', 1)]
	state_noterminal1=[('E', 'E', 4)]
	state_terminal2=[('(', '(', 1)]
	state_noterminal2=[('E', 'E', 5)]
	state_terminal3=[]
	state_noterminal3=[('E', 'E', -2)]
	state_terminal4=[(')', ')', 6),('(', '(', 1)]
	state_noterminal4=[('E', 'E', 5)]
	state_terminal5=[]
	state_noterminal5=[('E', 'E', -2)]
	state_terminal6=[]
	state_noterminal6=[('E', 'E', -3)]
	avtomat.terminal=[state_terminal0,state_terminal1,state_terminal2,state_terminal3,state_terminal4,state_terminal5,state_terminal6]
	avtomat.noterminal=[state_noterminal0,state_noterminal1,state_noterminal2,state_noterminal3,state_noterminal4,state_noterminal5,state_noterminal6]
	return avtomat



avtomat=avtomat_init_0()
print(avtomat.check("((((()(()()()()()())))))"))



"""
for i in func?X:
        funcq(func(i))==i

"""
