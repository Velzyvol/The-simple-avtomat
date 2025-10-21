from  pyavtomat import *

def avtomat_init_0():
	avtomat=LR0Avtomat()
	state_terminal0=[('(', '(', 1)]
	state_noterminal0=[('S', 'S', 2)]
	state_terminal1=[(')', ')', 3)]
	state_noterminal1=[('S', 'S', 4)]
	state_terminal2=[('(', '(', 5)]
	state_noterminal2=[]
	state_terminal3=[]
	state_noterminal3=[('S', 'S', -2)]
	state_terminal4=[(')', ')', 6)]
	state_noterminal4=[]
	state_terminal5=[(')', ')', 7)]
	state_noterminal5=[]
	state_terminal6=[]
	state_noterminal6=[('S', 'S', -3)]
	state_terminal7=[]
	state_noterminal7=[('S', 'S', -3)]
	avtomat.terminal=[state_terminal0,state_terminal1,state_terminal2,state_terminal3,state_terminal4,state_terminal5,state_terminal6,state_terminal7]
	avtomat.noterminal=[state_noterminal0,state_noterminal1,state_noterminal2,state_noterminal3,state_noterminal4,state_noterminal5,state_noterminal6,state_noterminal7]
	return avtomat


avtomat=avtomat_init_0()

print(avtomat.check("()()"))
"""
for i in func?X:
        funcq(func(i))==i

"""
