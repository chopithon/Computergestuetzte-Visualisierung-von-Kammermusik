# source: https://web.mit.edu/music21/doc/moduleReference/moduleChord.html

from music21 import *

file = corpus.parse('bwv66.6')
allChords = []

def get_chords(input):
    sChords = input.chordify()
    sFlat = sChords.flatten()
    sOnlyChords = sFlat.getElementsByClass('Chord')

    for i in sOnlyChords:
        allChords.append(i.pitchedCommonName)

for i in allChords:
    print(i)