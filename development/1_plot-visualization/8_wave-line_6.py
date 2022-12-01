import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
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

# ANIMATION FUNCTION
def func(num, dataSet, line, redDots):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(dataSet[0:2, :num])    
    line.set_3d_properties(dataSet[2, :num])    
    redDots.set_data(dataSet[0:2, :num])    
    redDots.set_3d_properties(dataSet[2, :num]) 
    return line

# line: 1
y = np.arange(0,20,0.2)
x = np.cos(y)-1
z = 1/2*(np.cos(2*y)-1)
y = y * 0
dataSet = np.array([x, y, z])
numDataPoints = len(y)

c1 = ax.plot_surface(x, y, z, label = "c1")
c1._facecolors2d = c1._facecolor3d
c1._edgecolors2d = c1._edgecolor3d

"""
x, y = create_grid(-10, 10, 1)
z1 = np.zeros((20, 20))

c1 = ax.plot_surface(x, y, z1, label = "c1")
c1._facecolors2d = c1._facecolor3d
c1._edgecolors2d = c1._edgecolor3d
"""

# wave: 2
x, y = create_grid(-10, 10, 1)
z2 = np.cos(freq * x * np.pi / 3) * ampl
z2 = np.maximum(z, z2)
ax = fig.gca(projection='3d')

c2 = ax.plot_surface(x, y, z2, label = "c2")
c2._facecolors2d = c2._facecolor3d
c2._edgecolors2d = c2._edgecolor3d

plt.show()

# source: https://stackoverflow.com/questions/55531760/is-there-a-way-to-label-multiple-3d-surfaces-in-matplotlib 