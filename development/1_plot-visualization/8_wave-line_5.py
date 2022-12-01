# facecolors2d = facecolors3d
# problem: line 25: ValueError: Argument Z must be 2-dimensional. [doesn't even plot]

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')
plt.rcParams['legend.fontsize'] = 10

freq = 1.5 #frequence
ampl = 0.5 #amplitude
color = "red"

g2 = np.arange(-10,10,1)
g3 = np.arange(-10,10,1)

# First constraint
G2,G3 = np.meshgrid(g2,g3)
G4_1 = np.cos(freq*g2* np.pi/3)*ampl

ax = fig.gca(projection='3d')

c1 = ax.plot_surface(G2, G3, G4_1, label = "c1")
c1._facecolors2d = c1._facecolor3d
c1._edgecolors2d = c1._edgecolor3d

# Second
G3, G4 = np.meshgrid(g2, g3)
G2 = G3
c2 = ax.plot_surface(G2, G3, G4, label = "c2")
c2._facecolors2d = c2._facecolor3d
c2._edgecolors2d = c2._edgecolor3d

plt.show()

# source: https://stackoverflow.com/questions/55531760/is-there-a-way-to-label-multiple-3d-surfaces-in-matplotlib 