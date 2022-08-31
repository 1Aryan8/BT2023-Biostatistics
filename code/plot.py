import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.02)
y = np.exp(-pow(x, 2))

plt.title('Plot of a Basic Error function')
plt.plot(x, y)
plt.show()