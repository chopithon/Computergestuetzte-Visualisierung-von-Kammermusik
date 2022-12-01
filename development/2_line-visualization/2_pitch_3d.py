from re import X
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mido import MidiFile

fig = plt.figure()
mid = MidiFile('bach_cello-suite-1.mid')

def f(x, y):
    return np.sin(x) + np.cos(y)

mididict = []
pitch = []
x = []
y = []
z = []

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

num = 0 
for index in range(0, len(y)):
    z.append(0)

im = plt.imshow(f(x, y), animated=True)

x_b = []
y_b = []
z_b = []

x_b.extend(x)
y_b.extend(y)
z_b.extend(z)

x_a = x[:20]
y_a = y[:20]
z_a = z[:20]

def updatefig(*args):
    global x, y
    x += np.pi / 15.
    y += np.pi / 20.
    im.set_array(f(x, y))
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()