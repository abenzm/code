import numpy as np

A = np.mat("0 1 2; 1 0 3; 4 -3 8")
print "A\n", A

inverse = np.linalg.inv(A)
print "inverse of A\n", inverse

print "A * inverse of A\n", A * inverse
