#>>floor python-3-11-4
from  pyavtomat import *

def avtomat_init_0():
	avtomat=LR0Avtomat()
	state_terminal0=[('a', 'z', 2)]
	state_noterminal0=[('E', 'E', 1)]
	state_terminal1=[('a', 'z', 3)]
	state_noterminal1=[]
	state_terminal2=[]
	state_noterminal2=[('E', 'E', -1)]
	state_terminal3=[]
	state_noterminal3=[('E', 'E', -2)]
	avtomat.terminal=[state_terminal0,state_terminal1,state_terminal2,state_terminal3]
	avtomat.noterminal=[state_noterminal0,state_noterminal1,state_noterminal2,state_noterminal3]
	return avtomat

x=10
print(x[12:])

avtomat=avtomat_init_0()
print(avtomat.check("asdfsafd"))



"""
for i in func?X:
        funcq(func(i))==i

"""
