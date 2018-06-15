import numpy as np
import numpy.linalg as la
import time

X = np.array([range(0, 500), range(500, 1000)])
m, n = X.shape

t = time.time()
D = np.zeros([n, n])
for i in xrange(n):
    for j in xrange(i + 1, n):
        D[i, j] = la.norm(X[:, i] - X[:, j]) ** 2
        D[j, i] = D[i, j]
print time.time() - t

t = time.time()
D = np.zeros([n, n])
for i in xrange(n):
    for j in xrange(i + 1, n):
        d = X[:, i] - X[:, j]
        D[i, j] = np.dot(d, d)
        D[j, i] = D[i, j]
print time.time() - t

t = time.time()
G = np.dot(X.T, X)
D = np.zeros([n, n])
for i in xrange(n):
    for j in xrange(i + 1, n):
        D[i, j] = G[i, i] - G[i, j] * 2 + G[j,j]
        D[j, i] = D[i, j]
print time.time() - t

t = time.time()
G = np.dot(X.T, X)
H = np.tile(np.diag(G), (n, 1))
D = H + H.T - G * 2
print time.time() - t
