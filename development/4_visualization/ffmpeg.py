import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams['animation.ffmpeg_path'] ='C:\\ffmpeg\\bin\\ffmpeg.exe'
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")

x=np.linspace(100,150,100)
t=(x-100)/0.5
y=-.01*np.cos(t)+.5*np.sin(t)+100.01
z=.01*np.sin(t)+.5*np.cos(t)+99.5

def animate(i):
    line.set_data(x[:i],y[:i])
    line.set_3d_properties(z[:i])

ax.set_xlim3d([min(x),max(x)])
ax.set_ylim3d([min(y),max(y)])
ax.set_zlim3d([min(z),max(z)])
ax.set_title("Particle in magnetic field") 
ax.set_xlabel("X")
ax.set_xlabel("Y")
ax.set_xlabel("Z")
line,=ax.plot([],[],[])
lin_ani=animation.FuncAnimation(fig,animate)
plt.legend()

FFwriter = animation.FFMpegWriter(fps=10)
lin_ani.save('animation.mp4', writer = FFwriter)
# plt.show()