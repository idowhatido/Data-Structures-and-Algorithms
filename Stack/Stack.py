#This is a normal python list which can be used a stack with the
#help of append and pop functions

stack = []
stack.append(19)
stack.append(19)
stack.append(19)
stack.pop()



#As python list is a dynamic array the reallocation of memory is
#quite expensive everytime list exceeds defined memory limit
#Hence there is library specially dedicated in python for queues

from collections import deque
stack = deque()
stack.append(19)  
stack.append(13)
stack.append(11)
stack.pop()
print(stack)



