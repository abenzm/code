import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys

t = np.linspace(-np.pi, np.pi, 201)
print "t\n", t
k = np.arange(1, float(sys.argv[1]))
print "k1\n", k
k = 2 * k -1
print "k2\n", k
f = np.zeros_like(t)
print "f\n", f
for i in range(len(t)):
	f[i] = np.sum(np.sin(k * t[i])/k)
f = (4 * np.pi) * f

plot(t, f)
show()
