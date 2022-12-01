import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy

abbildung = plt.figure()
achsen = plt.axes(projection="3d")

freq = 1.5 #frequence
ampl = 0.5 #amplitude
color = "red"

x1 = numpy.linspace(-3, 3, 100)
y1 = numpy.linspace(-3, 3, 100)

z1 = numpy.cos(freq*x1* numpy.pi/3)*ampl
graph1 = achsen.plot(x1, y1, z1)

def schritt(i):
    z1= numpy.cos((freq*x1 + 1*i)* numpy.pi/3)*ampl
    graph1[0].set_data(x1, y1)
    graph1[0].set_3d_properties(z1)

animation = FuncAnimation(abbildung, schritt, interval=20)

plt.show()