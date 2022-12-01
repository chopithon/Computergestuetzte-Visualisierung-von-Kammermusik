"""
import mido
from mido import MidiFile

mid = MidiFile('vns_rnd.mid')

for i, track in enumerate(mid.tracks): #print out all messages in the file
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg["type"] == 'note_on' or msg["type"] == 'note_off':
            mido.tempo2bpm(msg.tempo)
        print(msg)
"""

from mido import MidiFile
import mido

mid = MidiFile('vns_rnd.mid')

mididict = []
output = []

for message in mid: #put all note on/off in midinote as dictionary.
    if message.type == 'note_on' or message.type == 'note_off' or message.type == 'time_signature':
        mididict.append(message.dict())

mem1=0
for msg in mididict: 

    mem1 = msg['time']
    if msg['type'] == 'note_on' and msg['velocity'] == 0: #make every note_on with 0 velocity note_off
        msg['type'] = 'note_off'

    if msg['type'] == 'note_on' or msg['type'] == 'note_off':
        msg['time'] = mido.tempo2bpm(msg['time'])

    mem2 = []
    if msg['type'] == 'note_on' or msg['type'] == 'note_off': #put note, starttime, stoptime, as nested list in a list. # format is [type, note, time, channel]
        mem2.append(msg['type'])
        mem2.append(msg['note'])
        mem2.append(msg['time'])
        mem2.append(msg['channel'])
        output.append(mem2)

    if msg['type'] == 'time_signature': #put timesignatures
        mem2.append(msg['type'])
        mem2.append(msg['numerator'])
        mem2.append(msg['denominator'])
        mem2.append(msg['time'])
        output.append(mem2)

for i in output:
    print(i)

print(mid.ticks_per_beat)