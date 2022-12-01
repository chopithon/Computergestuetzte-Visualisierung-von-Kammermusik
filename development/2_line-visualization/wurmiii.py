import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy

from mido import MidiFile

mid = MidiFile('bach_cello-suite-1.mid')

mididict = []
pitch = []

for i in mid: # put all note on/off in midinote as dictionary.
    if i.type == 'note_on' or i.type == 'note_off' or i.type == 'time_signature':
        mididict.append(i.dict())

mem1=0
for i in mididict: # change time values from delta to relative time.
    time = i['time'] + mem1
    i['time'] = time

    mem2 = []
    if i['type'] == 'note_on' or i['type'] == 'note_off': # put note, as nested list in a list. # format is [note]
        mem2.append(i['note'])
        pitch.append(mem2)

z_all = []
for i in pitch:
    for j in i:
        z_all.append(j)
 
abbildung = plt.figure()
achsen = plt.axes(projection="3d")

freq = 1.5 #frequence
ampl = 0.5 #amplitude
color = "red"

x2 = numpy.linspace(-50, 50, 100)
y2 = numpy.linspace(-50, 50, 100)
x2, y2 = numpy.meshgrid(x2, y2)
y2 *= 0.07

i = numpy.full(100, 1)
j = numpy.full(100, 1)
i, j = numpy.meshgrid(i, j)
z2= numpy.cos(freq * numpy.pi/3) * ampl * i

achsen.plot_surface(x2, y2, z2, color = color)

def schritt(i):
    z2= numpy.cos((freq*x2 + 1*i)* numpy.pi/3)*ampl
    achsen.clear()
    achsen.plot_surface(x2, y2, z2, color = color)
    achsen.set_zlim(0, 100)
    achsen.set_xlim(-50, 50)
    achsen.set_ylim(-50, 50)
    achsen.set_box_aspect((1, 1, 1))
  
ani = animation.FuncAnimation(abbildung, schritt, interval = 30, blit = False)

plt.show()