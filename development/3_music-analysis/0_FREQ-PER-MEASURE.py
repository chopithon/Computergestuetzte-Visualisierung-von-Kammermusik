from mido import MidiFile

mid = MidiFile('bth-trio.mid')

mididict = []
pitch = []
outer = [] # time signature

ticks_per_beat = mid.ticks_per_beat
count_ticks = 0 # counts ticks of a measure

def get_ticks_per_measure(denominator, numerator):
    global ticks_per_beat
    if denominator == 4:
        ticks_per_measure = ticks_per_beat * numerator
        #print("Taktart:", msg["numerator"], "/", msg["denominator"])

    elif denominator == 8:
        ticks_per_beat /= 2 # get ticks per quaver
        ticks_per_measure = ticks_per_beat * numerator
        #print("Taktart:", msg["numerator"], "/", msg["denominator"])

    elif denominator == 16:
        ticks_per_beat /= 4 # get ticks per sixteen
        ticks_per_measure = ticks_per_beat * numerator
        #print("Taktart:", msg["numerator"], "/", msg["denominator"])

    elif denominator == 2:
        ticks_per_beat *= 2 # get ticks per half
        ticks_per_measure = ticks_per_beat * numerator
        #print("Taktart:", msg["numerator"], "/", msg["denominator"])
    
    return ticks_per_measure

for message in mid: #put all note on/off in midinote as dictionary.
    if message.type == 'note_on' or message.type == 'note_off' or message.type == 'time_signature':
        mididict.append(message.dict())

mem1=0
for msg in mididict: 

    mem1 = msg['time']
    if msg['type'] == 'note_on' and msg['velocity'] == 0: #make every note_on with 0 velocity note_off
        msg['type'] = 'note_off'

    mem3 = []
    if msg['type'] == 'time_signature': #put timesignatures
        denominator = msg["denominator"]
        numerator = msg["numerator"]

        ticks_per_measure = get_ticks_per_measure(denominator, numerator)
        outer.append(ticks_per_measure)

    mem2 = []
    if msg['type'] == 'note_on' or msg['type'] == 'note_off': #put note, starttime, stoptime, as nested list in a list. # format is [type, note, time, channel]
        mem2.append(msg['type'])
        mem2.append(msg['note'])
        mem2.append(msg['time'])
        mem2.append(msg['channel'])
        pitch.append(mem2)

        count_ticks += msg['time']
        if count_ticks >= ticks_per_measure:
            pitch.append("True")
            count_ticks = 0

print(outer)
count = 0
while count < 100:
    print(pitch[count])
    count += 1
    
print(mid.ticks_per_beat)