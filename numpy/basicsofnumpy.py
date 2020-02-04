import numpy as np

A = np.array([1,3,5,7])

#print(A)
matrix1 = np.mat([ [1.0,2,7], [3,4,5] ])
print(matrix1)

# print('shape:',matrix.shape)
# #gives the dimension of array, for a matrix with n rows and m cols
# # shape will be (n,m)
# print('size:',matrix.size)
# #gives the total number of elements of the array, is equal to the 
# #product of the elements of shape
# print('data type:',matrix.dtype )
# # gives the type of elements in the array
# print('size:',matrix.itemsize )
# #gives the size in bytes 

matrix2 = np.arange(6).reshape(2,3)
print(matrix2)
total = matrix1 + matrix2
print(total)
difference = matrix1 - matrix2
print(difference)
A = np.array([[2,3],[4,5]])
B = np.array([[1,2],[3,4]])
print(A)
product = A.dot(A)
print('The product is:',product)
product = A * B
print('The product is:',product)
#determinant
print('Determinant of B is\n',np.linalg.det(B))
#transpose
print('Transpose of B is\n',np.matrix.transpose(B))
