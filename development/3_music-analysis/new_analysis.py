"""
from mido import MidiFile

mid = MidiFile('1_bth-str-trio.mid')

mididict = []
instr_information = []

for i, track in enumerate(mid.tracks):
    for msg in track:
        if msg.type == "note_on" or msg.type == "note_off":
            mem1 = []
            mem1.append(msg.type)
            mem1.append(msg.channel)
            mem1.append(msg.note)
            mem1.append(msg.velocity)
            mem1.append(msg.time)
            instr_information.append(mem1)

count = 0
while count < 100:
    print(instr_information[count])
    count += 1
"""
from music21 import *
file = converter.parse('1_bth-str-trio.mid')
allChords = []
sChords = file.chordify()
sFlat = sChords.flatten()
sOnlyChords = sFlat.getElementsByClass('Chord')
for i in sOnlyChords:
	allChords.append(i.pitchedCommonName)
print(allChords)