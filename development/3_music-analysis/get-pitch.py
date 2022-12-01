# https://stackoverflow.com/questions/36647054/music21-getting-all-notes-with-durations


from music21 import *

file = converter.parse('vns_rnd.mid')
notes = []

for n in file.pitches:
    notes.append(n)

print(notes)