import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy

abbildung = plt.figure()
achsen = plt.axes(projection="3d")

x = numpy.linspace(-3, 3, 100)
y = numpy.linspace(-3, 3, 100)
x , y = numpy.meshgrid(x, y)

z = numpy.sin(x)
achsen.plot_surface(x, y, z, color = "red")

def schritt(i):
	z = numpy.sin(x + i)
	achsen.clear()
	achsen.plot_surface(x, y, z, color = "red")

ani = animation.FuncAnimation(abbildung, schritt, interval = 30, blit = False)

plt.show()