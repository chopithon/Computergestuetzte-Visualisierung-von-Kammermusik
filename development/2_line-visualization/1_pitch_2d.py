import matplotlib.pyplot as plt
import numpy as np
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

for i in pitch:
    y.append(i)

num = 0
for index in range(0, len(y)):
    x.append(num)
    num += 1

fig, ax = plt.subplots()
ax.plot(x, y)

ax.grid()

fig.savefig("test.png")
plt.show()