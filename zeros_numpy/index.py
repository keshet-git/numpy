import numpy as np 

#z = np.zeros((2, 3))
#print(z)

x = np.ones((4, 5))
#print(x)
f = np.identity(4)
#print(f)
p = np.empty((2,2))

#print(p)
first = np.ones((2, 2))
second = first
second[0,0] =9
print(first)