import numpy as np
a = np.arange(6).reshape(1, 6)
print(a)

# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])

print(a.shape)
#(3, 5)
print('size:',a.ndim)
#2
print(a.dtype.name)
#'int64'
print(a.itemsize)
#8
print(a.size)
#15
print(type(a))
# <type 'numpy.ndarray'>
# >>> b = np.array([6, 7, 8])
# >>> b
# array([6, 7, 8])
# >>> type(b)
# <type 'numpy.ndarray'>