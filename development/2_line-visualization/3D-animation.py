import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy

abbildung = plt.figure()
achsen = plt.axes(projection="3d")

x = numpy.linspace(-3, 3, 100)
y = numpy.linspace(-3, 3, 100)
x, y = numpy.meshgrid(x, y)

z = numpy.cos(x)
achsen.plot_surface(x, y, z)

def schritt(i):
    z = numpy.cos(x + 0.02 * i)
    achsen.clear()
    achsen.plot_surface(x, y, z)

animation = FuncAnimation(abbildung, schritt, interval=20)

plt.show()