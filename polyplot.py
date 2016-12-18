import numpy as np
import matplotlib.pyplot as plt

func = np.poly1d(np.array([39,63,113,54]).astype(float))
x = np.linspace(-10, 10, 30)
y = func(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
