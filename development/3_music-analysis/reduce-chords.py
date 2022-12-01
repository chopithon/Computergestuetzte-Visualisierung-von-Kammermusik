from music21 import *

def demoMakeChords():
    # wtc no 1
    #src = corpus.parse('bwv65.2').measures(0, 5)
    src = corpus.parse('opus18no1/movement3.xml').measures(0, 10)
    src.flattenParts().makeChords(minimumWindowSize=3).show()


    src = corpus.parse('opus18no1/movement3.xml').measures(0, 10)
    src.chordify().show()

print(demoMakeChords())