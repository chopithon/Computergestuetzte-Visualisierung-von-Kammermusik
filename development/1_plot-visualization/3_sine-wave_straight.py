import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-np.pi, np.pi, 30)
y = x
x,y = np.meshgrid(x,y)
z = 2*np.sin(y)
surf = ax.plot_surface(x,y,z)

plt.show()