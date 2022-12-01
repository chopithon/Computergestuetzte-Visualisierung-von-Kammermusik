# ros, 05.06.22

# facecolors2d = facecolors3d
# problem: line 25: ValueError: Argument Z must be 2-dimensional. [doesn't even plot]

# facecolors2d = facecolors3d
# problem: line 25: ValueError: Argument Z must be 2-dimensional. [doesn't even plot]

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')
plt.rcParams['legend.fontsize'] = 10

freq = 1.5 #frequence
ampl = 0.2 #amplitude
color = "red"


def create_grid(min, max, step):
    x = np.arange(min, max, step)
    y = np.arange(min, max, step)
    return np.meshgrid(x, y)


x, y = create_grid(-10, 10, 1)

z2 = np.zeros((20, 20))
# Second
c2 = ax.plot_surface(x, y, z2, label = "c2")
c2._facecolors2d = c2._facecolor3d
c2._edgecolors2d = c2._edgecolor3d


z1 = np.cos(freq * x * np.pi / 3) * ampl

z1 = np.maximum(z1, z2)
ax = fig.gca(projection='3d')


c1 = ax.plot_surface(x, y, z1, label = "c1")
c1._facecolors2d = c1._facecolor3d
c1._edgecolors2d = c1._edgecolor3d

plt.show()

# source: https://stackoverflow.com/questions/55531760/is-there-a-way-to-label-multiple-3d-surfaces-in-matplotlib 