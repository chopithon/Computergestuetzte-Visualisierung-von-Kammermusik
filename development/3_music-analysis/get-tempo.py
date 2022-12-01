import mido
from mido import MidiFile

mid = MidiFile('vns_rnd.mid')
for msg in mid:
    if msg.type == 'set_tempo':
        tempo_bpm = mido.tempo2bpm(msg.tempo)
        print('Tempo set to', int(tempo_bpm))

