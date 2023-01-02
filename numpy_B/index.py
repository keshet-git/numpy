import numpy as np

#a_mul = np.array([[[1,2,3, 1],
 #               [4,5,6, 1],
  #              [7,8,8, 1]],
   #             [[1,1,1,1],
    #            [1,1,1,1],
     #           [1,1,1,1]]])

#print(a_mul.shape)
#print(a_mul.ndim)
#print(a_mul.size)
#print(a_mul.dtype)

#a = np.array([[1,2,3],
 #           [4,"5",6],
  #          [7,8,9]],dtype=np.float32)

#d = {'1': 'A'}

#a = np.array([[1,2,3],
 #           [4,d,6],
  #          [7,8,"Hello"]])

a = np.array([[1,2,3],
            [4,5,6],
            [7,8,9]], dtype="<U")
print(a.dtype)
#print(a[1][1].dtype)
#print(a[1,1])
print(type(a[1][0]))