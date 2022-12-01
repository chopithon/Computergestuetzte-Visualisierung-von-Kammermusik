from music21 import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
 
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_box_aspect((1, 1, 1))

def open_midi(midi_path):
    mf = midi.MidiFile()
    mf.open(midi_path)
    mf.read()
    mf.close()         

    return midi.translate.midiFileToStream(mf)

base_midi = open_midi("bth-trio.mid")

sChords = open_midi("bth-trio.mid").chordify()
sFlat = sChords.flatten()
sOnlyChords = sFlat.getElementsByClass('Chord')
displayPart = stream.Part(id='displayPart')

for i in range(0, len(sOnlyChords) - 1):
    thisChord = sOnlyChords[i]
    nextChord = sOnlyChords[i + 1]

def appendChordPairs(thisChord, nextChord):
    if ((thisChord.isTriad() is True or
            thisChord.isSeventh() is True) and
                thisChord.root().name == 'A'):
        closePositionThisChord = thisChord.closedPosition(forceOctave=4)
        closePositionNextChord = nextChord.closedPosition(forceOctave=4)

        m = stream.Measure()
        m.append(closePositionThisChord)
        m.append(closePositionNextChord)
        displayPart.append(m)

allChords = []
allColors = []

for i in range(len(sOnlyChords) - 1):
    thisChord = sOnlyChords[i]
    basedChord = thisChord.bass()
    namedChord = basedChord.name
    strChord = str(namedChord)

    allChords.append(strChord)

    nextChord = sOnlyChords[i + 1]
    appendChordPairs(thisChord, nextChord)

for i in range(len(allChords)):
    if i == "B-":
        color = "blue"
        allColors.append(color)
    
    elif i == "F":
        color = "green"
        allColors.append(color)

    else:
        allColors.append("red")

freq = 1.5 
ampl = 0.5 

x1= np.arange(-10,10,1)
y1= np.arange(-10,10,1)

x1,y1= np.meshgrid(x1,y1)
z1= np.cos(freq*x1* np.pi/3)*ampl

color = "red"

ax.plot_surface(x1, y1, z1, color=color)

ax.set_zlim(0, 20)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

numColor = 0

def step(i):
    z1= np.cos((freq*x1 + 1*i)* np.pi/3)*ampl
    ax.clear()
    ax.plot_surface(x1, y1, z1, color=allColors[0])
    allColors.remove[0]
    ax.set_zlim(0, 20)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_box_aspect((1, 1, 1))

    
ani = animation.FuncAnimation(fig, step, interval = 30, blit = False)

plt.show()