import numpy as np

#print(np.nan)
#print(np.inf)

#print(np.isnan(np.sqrt(-1)))
#print(np.isinf(np.array([10]) / 0))

#print(np.sqrt(-1))
#print(np.array([10]) / 0)

l1 =[1,2,3,4,5]
l2 = [6,7,8,9,0]

a1 = np.array(l1)
a2 = np.array(l2)

#print(l1 + l2)
#print(a1 * 5)

#print(a1 + a2)
r1 = np.array([1,2,3])
r2 = np.array([[1],
            [2]])
#print(r1 + r2)

s1 = np.array([[1,2,3],
            [4,5,6]])
#print(np.sqrt(s1))

x = np.array([1,2,3])
x = np.append(x, [7,8,9])
#print(x)

#print(np.delete(s1, 1))
#print(np.delete(s1, 3))
#print(np.delete(s1, 4))

#print(np.delete(s1, 0, 0))

print(np.delete(s1, 1, 1))