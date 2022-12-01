import matplotlib.pyplot as plt
import numpy

abbildung = plt.figure()
achsen = plt.axes(projection="3d")

start_value = -40

x1 = numpy.linspace(-50, 50, 100)
y1 = [numpy.linspace(-18, -22, 100)]
x1, y1 = numpy.meshgrid(x1, y1)

z1 = numpy.cos(5.2*x1* numpy.pi/3)*3


def plot_lines(start_value, thickness):
    x1 = numpy.linspace(-50, 50, 100)
    y1_max = start_value + thickness
    y1_min = start_value - thickness
    y1 = numpy.linspace(y1_max, y1_min, 100)

    x1, y1 = numpy.meshgrid(x1, y1)
    z1 = numpy.cos(5.2*x1* numpy.pi/3)*3


    achsen.plot_surface(x1, y1, z1, color = "black")

while start_value <= 40:
    thickness = 0.5
    plot_lines(start_value, thickness)
    start_value += 10

plt.show()