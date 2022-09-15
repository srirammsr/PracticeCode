import numpy  as np
arr=np.array([[1,2,3],[34,56,8]])
# or
#arr=np.array([[1,2,3],[34,56,8]],dtype=float)

print(arr)
print(len(arr))
print(arr.ndim)
print(arr.shape)
print(arr.size)

a=np.arange(1,10,2)
print(a)

arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
 
newarr = arr.reshape(2, 2, 3)
print(newarr)
