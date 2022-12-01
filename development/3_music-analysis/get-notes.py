from music21 import *

def open_midi(midi_path):
    # There is an one-line method to read MIDIs
    # but to remove the drums we need to manipulate some
    # low level MIDI events.
    mf = midi.MidiFile()
    mf.open(midi_path)
    mf.read()
    mf.close()         

    return midi.translate.midiFileToStream(mf)

base_midi = open_midi("vns_rnd.mid")

count_channel = 0
while count_channel < 10: 
    s2 = instrument.partitionByInstrument(midi)
    notes_to_parse = s2.parts[count_channel].recurse()
    sIterator = base_midi.getElementsByClass(note.Note)
    sOut = sIterator.stream()
    print(sOut.show('text'))