# https://stackoverflow.com/questions/36647054/music21-getting-all-notes-with-durations

from music21 import *

allBach = corpus.search('bach')

"""
x = allBach[0]
p = x.parse()

partStream = p.parts.stream()
"""
def open_midi(midi_path):
    # There is an one-line method to read MIDIs
    # but to remove the drums we need to manipulate some
    # low level MIDI events.
    mf = midi.MidiFile()
    mf.open(midi_path)
    mf.read()
    mf.close()         

    return midi.translate.midiFileToStream(mf)

base_midi = open_midi("bth-trio.mid")
eventlist = midi.translate.chordToMidiEvents

stream.Part(id='displayPart')

"""
for n in base_midi.pitches:
    print("Pitch: " + str(n))

for n in base_midi.notes:
    print("Note: " + str(n))
#print "Duration " + str(x.parse().duration)
"""
