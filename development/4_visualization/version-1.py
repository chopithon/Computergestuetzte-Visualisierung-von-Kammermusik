import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy
from mido import MidiFile

# ----- music analysis -----
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

# ----- visualization -----
abbildung = plt.figure()
achsen = plt.axes(projection="3d")

# line
x1 = numpy.linspace(-50, 50, 100)
y1 = numpy.linspace(-18, -22, 100)
x1, y1 = numpy.meshgrid(x1, y1)
y1 *= 0.5

z_i = numpy.full(100, 1)
z_j = numpy.full(100, 1)
z_i, z_j = numpy.meshgrid(z_i, z_j)
z1 = z_all[:100] * z_i

graph1 = achsen.plot_surface(x1, y1, z1, color="black")

# plot 
freq = 5.2 #frequence
ampl = 3 #amplitude
color = "red"

x2 = numpy.linspace(-50, 50, 100)
y2 = numpy.linspace(-50, 50, 100)
x2, y2 = numpy.meshgrid(x2, y2)

z2= numpy.cos(freq*x2* numpy.pi/3)*ampl
graph2 = achsen.plot_surface(x2, y2, z2, color = color)

count = 100
def schritt(i):
    global count, z1
    achsen.clear()
    
    # line
    global count, z, y, z_new

    if count < len(z_all):
        if count != 100:
            z1 = z_new
        
        z_list = z1.tolist()
        
        for k in z_list:
            k.pop(0)
            k.append(z_all[count])
        
        z_new = numpy.array(z_list)
        count += 1

    achsen.plot_surface(x1, y1, z_new, color = "black")

    # plot
    z2 = numpy.cos((freq*x2 + 1*i)* numpy.pi/3)*ampl
    achsen.plot_surface(x2, y2, z2, color = color)

    achsen.set_zlim(0, 100)
    achsen.set_xlim(-50, 50)
    achsen.set_ylim(-50, 50)
    achsen.set_box_aspect((1, 1, 1))

animation = FuncAnimation(abbildung, schritt, interval=20, blit = False)

plt.show()