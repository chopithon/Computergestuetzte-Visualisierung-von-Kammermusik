# two surf functions/ variables
# problem: line 61: AttributeError: 'int' object has no attribute 'ndim' [doesn't even plot]

# importing matplotlib.pyplot from
# python
import matplotlib.pyplot as plt
 
# importing numpy package from
# python
import numpy as np
 
# creating a range of values for
# x,y,x1,y1  from -5 to 5 with
# a space of 1 between the elements
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
 
# creating a range of values for
# x,y,x1,y1  from -5 to 5 with
# a space of 0.6 between the elements
x1= np.linspace(-2, 2, 100)
y1= np.linspace(-2, 2, 100)
 
# Creating a mesh grid with x ,y and x1,
# y1 which creates an n-dimensional
# array
x, y = np.meshgrid(x, y)
x1,y1= np.meshgrid(x1,y1)
 
# Creating a sine function with the
# range of values from the meshgrid
z = 0

# Creating a cosine function with the
# range of values from the meshgrid
z1= np.linspace(-2, 2, 100)

"""
def append_zero(list, element):
    i = 0
    while i < 100:
        list.append(element)
        i += 1

append_zero(y, 0)
append_zero(z, 0)

append_zero(x1, 1)
append_zero(y1, 1)
append_zero(z1, 1)
"""
 
# Creating an empty figure for
# 3D plotting
fig = plt.figure()
 
# using fig.gca, we are creating a 3D
# projection plot in the empty figure
ax = fig.gca(projection="3d")
 
# Creating a wireframe plot with the x,y and
# z-coordinates respectively along with the
# color as red
surf = ax.plot_wireframe(x, y, z, color="red")
 
# Creating a wireframe plot with the points
# x1,y1,z1 along with the plot line as green
surf1 = ax.plot_wireframe(x1, y1, z1, color="green")
 
#showing the above plot
plt.show()

"""
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

x_line = np.linspace(-2, 2, 100)
y_line = []
z_line = []

x_lini = []
y_lini = []
z_lini = []

def append_zero(list):
    i = 0
    while i < 100:
        list.append(0)
        i += 1

append_zero(y_line)
append_zero(z_line)

append_zero(x_lini)
append_zero(y_lini)
append_zero(z_lini)

surf = ax.plot(x_line, y_line, z_line, color="orange")
surf1 = ax.plot(x_lini, y_lini, z_lini, color="red")
plt.show()
"""

# source: GeeksForGeeks: Examples of 3D plotting: Example 2: https://www.geeksforgeeks.org/introduction-to-3d-plotting-with-matplotlib/ (23.06.22)