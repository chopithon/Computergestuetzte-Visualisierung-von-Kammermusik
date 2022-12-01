#ros, 22.06.22

#importing matplotlib.pyplot from
# python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
# importing numpy package from python
import numpy as np
 
# creating an empty figure for plotting
fig = plt.figure()
 
# defining a sub-plot with 1x2 axis and defining
# it as first plot with projection as 3D
ax = fig.add_subplot(1, 1, 1, projection='3d')


# creating a range of values for
# x1,y1  from -1 to 1 with
# a space of 0.1 between the elements so that
# we can create a single curve in the plot
x1= np.arange(-10,10,1)
y1= np.arange(-10,10,1)

# Creating a mesh grid with x ,y and x1,
# y1 which creates an n-dimensional
# array
x1,y1= np.meshgrid(x1,y1)
 
# Creating a cosine function with the
# range of values from the meshgrid
z1= np.cos(x1* np.pi/2)
 
 

# Creating a wireframe plot with the points
# x1,y1,z1 along with the plot line as red
ax.plot_surface(x1, y1, z1, color="red")

ax.set_zlim(0, 3)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

def step(i):
    z1= np.cos((x1 + 1*i)* np.pi/4)
    ax.clear()
    ax.plot_surface(x1, y1, z1, color="red")
    ax.set_zlim(0, 3)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    
ani = animation.FuncAnimation(fig, step, interval = 30, blit = False)

 
# Showing the above plot
plt.show()

#source: GeeksForGeeks: Introduction to 3D Plotting with Matplotlib: Key 3D Plots using Matplotlib: 
# https://www.geeksforgeeks.org/introduction-to-3d-plotting-with-matplotlib/ (22.06.22) 
