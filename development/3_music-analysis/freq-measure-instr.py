from mido import MidiFile

mid = MidiFile('vns_rnd.mid')

mididict = []
output = []
pitch_0 = []
pitch_1 = []
pitch_2 = []
pitch_3 = []
pitch_4 = []
pitch_5 = []
pitch_6 = []
pitch_7 = []
pitch_8 = []
pitch_9 = []
pitch_10 = []
pitch_11 = []
pitch_12 = []
pitch_13 = []
pitch_14 = []
pitch_15 = []

ticks_per_beat = mid.ticks_per_beat
count_ticks = 0 # counts ticks of a measure

for i in mid: #put all note on/off in midinote as dictionary.
    if i.type == 'note_on' or i.type == 'note_off' or i.type == 'time_signature':
        mididict.append(i.dict())

def get_ticks_per_measure(msg):
    global ticks_per_beat
    if msg["denominator"] == 4:
        ticks_per_measure = ticks_per_beat * msg["numerator"]
        print("Taktart:", msg["numerator"], "/", msg["denominator"])

    elif msg["denominator"] == 8:
        ticks_per_beat /= 2 # get ticks per quaver
        ticks_per_measure = ticks_per_beat * msg["numerator"]
        print("Taktart:", msg["numerator"], "/", msg["denominator"])

    elif msg["denominator"] == 16:
        ticks_per_beat /= 4 # get ticks per sixteen
        ticks_per_measure = ticks_per_beat * msg["numerator"]
        print("Taktart:", msg["numerator"], "/", msg["denominator"])

    elif msg["denominator"] == 2:
        ticks_per_beat *= 2 # get ticks per half
        ticks_per_measure = ticks_per_beat * msg["numerator"]
        print("Taktart:", msg["numerator"], "/", msg["denominator"])
    
    return ticks_per_measure

mem1=0
for i in mididict: #change time values from delta to relative time.
    time = i['time'] + mem1
    i['time'] = time

    mem1 = i['time']
    if i['type'] == 'note_on' and i['velocity'] == 0: #make every note_on with 0 velocity note_off
        i['type'] = 'note_off'

    if i['type'] == 'time_signature': #put timesignatures
        ticks_per_measure = get_ticks_per_measure(i)

    mem2 = []
    if i['type'] == 'note_on' or i['type'] == 'note_off': #put note, starttime, stoptime, as nested list in a list. # format is [type, note, time, channel]
        if i["channel"] == 0:
            pitch_0.append(i['note'])

            count_ticks += i['time']
            if count_ticks >= ticks_per_measure:
                pitch_0.append("True")
                count_ticks = 0

        if i["channel"] == 1:
            pitch_1.append(i["note"])

        if i["channel"] == 2:
            pitch_2.append(i["note"])

        if i["channel"] == 3:
            pitch_3.append(i['note'])

        if i["channel"] == 4:
            pitch_4.append(i["note"])

        if i["channel"] == 5:
            pitch_5.append(i["note"])

        if i["channel"] == 6:
            pitch_6.append(i['note'])

        if i["channel"] == 7:
            pitch_7.append(i["note"])

        if i["channel"] == 8:
            pitch_8.append(i["note"])

        if i["channel"] == 9:
            pitch_9.append(i['note'])

        if i["channel"] == 10:
            pitch_10.append(i["note"])

        if i["channel"] == 11:
            pitch_11.append(i["note"])

        if i["channel"] == 12:
            pitch_12.append(i["note"])

        if i["channel"] == 13:
            pitch_13.append(i['note'])

        if i["channel"] == 14:
            pitch_14.append(i["note"])

        if i["channel"] == 15:
            pitch_15.append(i["note"])
    
print(pitch_0)
print(pitch_1)
print(pitch_2)
# print(mid.ticks_per_beat)