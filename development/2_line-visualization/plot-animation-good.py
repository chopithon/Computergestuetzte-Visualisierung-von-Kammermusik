import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy
 
abbildung = plt.figure()
achsen = plt.axes(projection="3d")

freq = 1.5 #frequence
ampl = 0.5 #amplitude
color = "red"

x2 = numpy.linspace(-3, 3, 100)
y2 = numpy.linspace(-3, 3, 100)
x2, y2 = numpy.meshgrid(x2, y2)

z2= numpy.cos(freq*x2* numpy.pi/3)*ampl
achsen.plot_surface(x2, y2, z2, color = color)

def schritt(i):
    z2= numpy.cos((freq*x2 + 1*i)* numpy.pi/3)*ampl
    achsen.clear()
    achsen.plot_surface(x2, y2, z2, color = color)
  
ani = animation.FuncAnimation(abbildung, schritt, interval = 30, blit = False)

plt.show()