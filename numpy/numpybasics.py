# Introduction to machine learning
# Author: Prastab Dhakal
# Chapter: Classes and objects

import numpy as np
from numpy import linalg as lin

X = np.array([1,2,3])
print(X)
Y = np.mat([1,2])
print(Y)
Z= np.mat([[3,2],[1,4]])
print(Z)
A = np.mat([1,2])

print(A+A)
print(A-A)
#print(A*A) #(dimension must be same)
print(Z*Z)


lin.det( Z ) #matrix must be a square matrix
print("The transpose of",Z,"is:\n",np.linalg.inv(Z))
print("The transpose of",Z,"is:\n",np.matrix.transpose(Z))
"""
import numpy as np
a = np.arange(15).reshape(3, 5)
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
"""
