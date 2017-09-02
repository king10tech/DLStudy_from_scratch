import numpy as np

A=np.array([[1,2],[3,4]]) # 2 by 2 matrix
B=np.array([[5,6],[7,8]]) # 2 by 2 matrix
C=np.dot(A,B) # ouput is also 2 by 2 matrix


print(C)


A_1=np.array([[1,2,3],[4,5,6]]) # 2 by 3 matrix
B_1=np.array([[1,2],[3,4],[5,6]]) # 3 by 2 matrix
C_1=np.dot(A_1,B_1)

print(C_1)

X=np.array([1,2]) # array
W=np.array([[1,2,3],[4,5,6]]) # 2 by 3 matrix
Y=np.dot(X,W) # output is array with 3 element

print(Y)