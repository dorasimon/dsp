# Matrix Algebra

import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
w = np.array([[1], [8], [0], [5]])

print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(v.shape)
print(w.shape)

print(u + v)
print(u - v)
print(np.dot(6, u))
print(np.dot(u, v))
print(np.sqrt(np.dot(u, u)))

print(A + C)
print(A - C.T)
print(C.T + 3 * D)
print(np.dot(B, A))
print(np.dot(B, A.T))
print(np.dot(B, C))
print(np.dot(C, B))
print(np.linalg.matrix_power(B, 4))
print(np.dot(A, A.T))
print(np.dot(D.T, D))
