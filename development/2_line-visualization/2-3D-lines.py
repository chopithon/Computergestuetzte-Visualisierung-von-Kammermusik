import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy

abbildung = plt.figure()
achsen = plt.axes(projection="3d")

x1 = numpy.linspace(-3, 3, 100)
y1 = numpy.full(100, 1)
z1 = 0.5 * numpy.sin(x1)
graph1 = achsen.plot(x1, y1, z1)

x2 = numpy.linspace(-3, 3, 100)
y2 = numpy.full(100, 0)
z2 = numpy.cos(x2)
graph2 = achsen.plot(x2, y2, z2)

def schritt(i):
    z1 = numpy.sin(x1 + 0.1 * i)
    graph1[0].set_data(x1, y1)
    graph1[0].set_3d_properties(z1)

    z2 = numpy.cos(x2 + 0.1 * i)
    graph2[0].set_data(x2, y2)
    graph2[0].set_3d_properties(z2)

animation = FuncAnimation(abbildung, schritt, interval=20)

plt.show()