import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

def data(i, z, line):
    z = np.sin(x+y+i)
    ax.clear()
    line = ax.plot_surface(x, y, z,color= 'b')
    return line,

f = 2 #frequence
n = f*np.pi #period
fig = plt.figure() #create new figure (here: surface)
ax = fig.add_subplot(111, projection='3d') #add 3D axes, position of coordinate system (https://ch.mathworks.com/help/matlab/ref/subplot.html)

x = np.linspace(0, n, 100) #return evenly spaced numbers over a specified interval (https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
y = np.linspace(0, n, 100) #return evenly spaced numbers over a specified interval (https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
x,y = np.meshgrid(x,y) #Return coordinate matrices from coordinate vectors (https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html)
z = np.sin(x+y)
line = ax.plot_surface(x, y, z,color= 'b')


zline = np.linspace(0, 15, 15)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')       

ani = animation.FuncAnimation(fig, data, fargs=(z, line), interval=30, blit=False)

plt.show()

#problem: the wave is not straight, the wave starts in the corner insted of on the x axe