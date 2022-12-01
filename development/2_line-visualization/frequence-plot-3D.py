import matplotlib.pyplot as plt
import numpy

from mido import MidiFile

mid = MidiFile('bach_cello-suite-1.mid')

mididict = []
pitch = []
x = []
y = []

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

print(z_all)

abbildung = plt.figure()
achsen = plt.axes(projection="3d")

x = numpy.linspace(-3, 3, 100)
y = numpy.full(100, 1)
z = z_all[:100]

achsen.plot(x, y, z)

plt.show()

