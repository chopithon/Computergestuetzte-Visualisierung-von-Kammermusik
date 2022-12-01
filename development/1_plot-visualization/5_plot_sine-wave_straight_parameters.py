import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

def data(i, z, line):
    z = f*np.cos(a*z+i)
    ax.clear()
    line = ax.plot_surface(x, y, z, color = c)
    return line,

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

f = 2 #frequence
a = 1 #amplitude
c = "b" #color

x = np.linspace(-np.pi, np.pi, 100)
y = x
x,y = np.meshgrid(x, y)
z = f*np.sin(y)
surf = ax.plot_surface(x, y, z)

line = ax.plot_surface(x, y, z, color = "b")
xline = np.linspace(0, 100, 100)
yline = xline
zline = np.sin(xline)

ax.plot3D(xline, yline, zline, "gray")
ani = animation.FuncAnimation(fig, data, fargs = (z, line), interval = 30, blit = False)
plt.show()