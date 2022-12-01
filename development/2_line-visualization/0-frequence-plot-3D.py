import matplotlib.pyplot as plt
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

x = numpy.linspace(-50, 50, 100)
y = numpy.linspace(-10, 10, 100)
x, y = numpy.meshgrid(x, y)
y *= 0.07

i = numpy.full(100, 1)
j = numpy.full(100, 1)
i, j = numpy.meshgrid(i, j)
z = z_all[:100] * i

graph = achsen.plot_surface(x, y, z)

achsen.set_zlim(0, 100)
achsen.set_xlim(-50, 50)
achsen.set_ylim(-50, 50)
achsen.set_box_aspect((1, 1, 1))

plt.show()