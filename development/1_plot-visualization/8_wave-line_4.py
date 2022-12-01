# create two functions (surface & line)
# problem: UserWarning: Animation was deleted without rendering anything. This is most likely unintended. 
# To prevent deletion, assign the Animation to a variable that exists for as long as you need the Animation. 
# [double animation -> animation 2 (line) would overwrite animation 1 (surface)]

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def surface():
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_box_aspect((1, 1, 1))

    freq = 1.5 
    ampl = 0.5 
    color = "red"

    x1= np.arange(-10,10,1)
    y1= np.arange(-10,10,1)
    x1,y1= np.meshgrid(x1,y1)
    z1= np.cos(freq*x1* np.pi/3)*ampl

    ax.plot_surface(x1, y1, z1, color=color)

    ax.set_zlim(0, 20)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    def step(i):
        z1= np.cos((freq*x1 + 1*i)* np.pi/3)*ampl
        ax.clear()
        ax.plot_surface(x1, y1, z1, color=color)
        ax.set_zlim(0, 20)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_box_aspect((1, 1, 1))

        
    ani = animation.FuncAnimation(fig, step, interval = 30, blit = False)


def line():
    fig1 = plt.figure()

    ax = fig1.add_subplot(1, 1, 1, projection='3d')
    ax.set_box_aspect((1, 1, 1))

    freq = 1.5 
    ampl = 0.5 
    color = "blue"

    x1= np.arange(-10,10,1)
    y1= np.arange(-10,10,1)
    x1,y1= np.meshgrid(x1,y1)
    z1= np.sin(freq*x1* np.pi/3)*ampl

    ax.plot_surface(x1, y1, z1, color=color)

    ax.set_zlim(0, 20)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    def step(i):
        z1= np.cos((freq*x1 + 1*i)* np.pi/3)*ampl
        ax.clear()
        ax.plot_surface(x1, y1, z1, color=color)
        ax.set_zlim(0, 20)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_box_aspect((1, 1, 1))

        
    ani1 = animation.FuncAnimation(fig1, step, interval = 30, blit = False)


surface()
line()