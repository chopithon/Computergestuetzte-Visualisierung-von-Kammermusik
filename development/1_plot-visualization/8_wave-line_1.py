# ax.plot (line) and plot_surface (surface)
# problem: programm plots only the surface (regardless the order of plot-call)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_box_aspect((1, 1, 1))

freq = 1.5 
ampl = 0.5 
color = "red"

# x-, y, z-coordinates of surface
x1= np.arange(-10,10,1)
y1= np.arange(-10,10,1)
x1,y1= np.meshgrid(x1,y1)
z1= np.cos(freq*x1* np.pi/3)*ampl

# x-, y, z-coordinates of line
x_line = []
y_line = []
z_line = []

def append_element(list, element):
    i = 0
    while i < 100:
        list.append(element)
        i += 1

append_element(x_line, 10)
append_element(y_line, 10)
append_element(z_line, 10)

ax.plot(x_line, y_line, z_line)
ax.plot_surface(x1, y1, z1, color=color)

ax.set_zlim(0, 20)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

def step(i):
    z1= np.cos((freq*x1 + 1*i)* np.pi/3)*ampl
    ax.clear()
    ax.plot(x_line, y_line, z_line)
    ax.plot_surface(x1, y1, z1, color=color)
    ax.set_zlim(0, 20)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_box_aspect((1, 1, 1))
   
ani = animation.FuncAnimation(fig, step, interval = 30, blit = False)

plt.show()