from music21 import *

file = 'bth-trio.mid'

midi = converter.parse(file)  
parts = instrument.partitionByInstrument(midi) 

notes_for_instruments = []
instruments = []
notes = []
chords = []

for i in range(len(parts.parts)): 
    notes_to_parse = parts.parts[i].recurse()
    instr = parts.parts[i].getInstrument()
    instruments.append(instr.instrumentName) 
    for element in notes_to_parse:   
        if isinstance(element, note.Note):  
        # if element is a note, extract pitch   
            notes.append(str(element.pitch))
        elif(isinstance(element, chord.Chord)):  
            # if element is a chord, append the normal form of the   
            # chord (a list of integers) to the list of notes.   
            chords.append('.'.join(str(n) for n in element.normalOrder))  
        elif isinstance(element, note.Rest):
            notes.append('Rest')

print(instruments)
#print(notes, chords)