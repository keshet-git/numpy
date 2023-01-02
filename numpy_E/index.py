import numpy as np

a = np.array([[1,2,3,4,5,6],
                [7,8,9,10,11,12],
                [13,14,15,16,17,18],
                [18,19,20,21,22,23]])

#print(a.min())
#print(a.max())
#print(a.mean())
#print(a.std())
#print(a.sum())
#print(np.median(a))

#print(a.shape)
#print(a.reshape(((5,4))))
#print(a.reshape((20,)))
#print(a.reshape((20,1)))
#print(a.reshape((2,10)))
#print(a.reshape((2, 2, 5)))
#print(a.reshape((2, 5, 2)))
#print(a.reshape((5, 2, 2)))
#print(a.flatten())
#print(a.ravel())

#var1 =a.flatten()
#var1[2] = 100
#print(var1)

#var = [v for v in a.flat]
#print(var)

#print(a.T)
#print(a.swapaxes(0, 1))

a1 = np.array([[1,2,3,4,5],
            [6,7,8,9,10]])
a2 = np.array([[11,12,13,14,15],
            [16,17,18,19,20]])

#s = np.concatenate((a1, a2), axis=1)
#print(s)

s = np.hstack((a1, a2))
#print(s)

numbers = np.random.choice([10,20,30,40,50], size=(5, 10))
print(numbers)