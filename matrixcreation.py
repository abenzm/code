import numpy as np

A = np.mat('1 2 3; 4 5 6; 7 8 9')
print "Create from string", A
print "Transpose A", A.T
print "Inverse A", A.I
print "Check inverse", A * A.I

print "Create from array", np.mat(np.arange(9).reshape(3, 3))

