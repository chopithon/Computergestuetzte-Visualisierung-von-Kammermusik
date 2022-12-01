import mido
from mido import MidiFile

mid = MidiFile('vns_rnd.mid')

for i, track in enumerate(mid.tracks): #print out all messages in the file
    print('Track {}: {}'.format(i, track.name))