# https://stackoverflow.com/questions/22612119/showing-midi-pitch-numbers-from-mid-file-with-music21

from music21 import *
import pickle

def get_notes():
    """ Get all the notes and chords from the midi files in the ./midi_songs directory """

    midi = converter.parse("bth-trio.mid")

    print("Parsing %s" % "bth-trio.mid")

    notes_to_parse = None

    count_channel = 0
    while count_channel < 10:
        notes = []
        try: # file has instrument parts
                s2 = instrument.partitionByInstrument(midi)
                notes_to_parse = s2.parts[count_channel].recurse() 
        except: # file has notes in a flat structure
                notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))
            
        """
            with open('data/notes', 'wb') as filepath:
            pickle.dump(notes, filepath)
        """

        print(notes)
        count_channel += 1

print(get_notes())