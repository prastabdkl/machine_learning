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
