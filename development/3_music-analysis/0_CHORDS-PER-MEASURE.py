# https://web.mit.edu/music21/doc/usersGuide/usersGuide_10_examples1.html#usersguide-10-examples1

from music21 import * 

file = converter.parse('1_bth-str-trio.mid')

sChords = file.chordify()
sFlat = sChords.flatten()
sOnlyChords = sFlat.getElementsByClass('Chord')
chords_per_measure = []

for c in sChords.getElementsByClass('Measure'):
    k = c.analyze('key')
    str_k = str(k)
    chords_per_measure.append(str_k)

print(chords_per_measure)