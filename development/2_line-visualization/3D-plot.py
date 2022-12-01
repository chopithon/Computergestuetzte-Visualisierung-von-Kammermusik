import matplotlib.pyplot as plt
import numpy

abbildung = plt.figure()
achsen = plt.axes(projection="3d")

x = numpy.linspace(-3, 3, 100)
y = numpy.full(100, 1)
z = 0.5 * numpy.square(x)

achsen.plot(x, y, z)

plt.show()