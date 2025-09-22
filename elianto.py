import numpy as np

M = np.array([[2, 9],
              [5, 7]])

N = np.array([[3, 4],
              [6, 1]])

print(M)
print(N)

s = M + N
print(s)

p = M * N
print(p)

r = np.dot(M, N)
print(r)
