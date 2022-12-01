from music21 import converter, instrument, note, chord, common
import pickle

file = converter.parse('vns_rnd.mid')

def get_notes():
    notes = []

    midi = converter.parse(file)

    print("Parsing %s" % file)

    notes_to_parse = None

    try:   
        s2 = instrument.partitionByInstrument(midi)
        notes_to_parse = s2.parts[0].recurse()
    except:  
        notes_to_parse = midi.flat.notes

    for element in notes_to_parse:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            print('.'.join(str(n) for n in element.normalOrder))
            notes.append('.'.join(str(n) for n in element.normalOrder))

    with open('data/notes', 'wb') as filepath:
        pickle.dump(notes, filepath)

    return notes

output = common.runParallel(parallelFunction=get_notes())