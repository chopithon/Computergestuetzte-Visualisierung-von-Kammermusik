from mido import MidiFile
import mido
from music21 import *

file_mid = MidiFile("bth-str-trio.mid")
file_stream = converter.parse("bth-str-trio.mid")

all_pitches = []
all_pitches_d = []
all_pitches_d_m = []
all_velocities = []
all_velocities_d = []

keys_per_measure = []
color_per_measure = []

count_ticks = 0
count_tracks = 0
count_measures_line = 0
measure_appended = False
msg_i = 0

# --- general information --- #
print("--- general information ---")
# key and ticks of file
key_file = file_stream.analyze("key")
print("key of piece: " + str(key_file))

ticks_per_beat = file_mid.ticks_per_beat
print("ticks per beat: " + str(ticks_per_beat))

thirty_second_ticks = file_mid.ticks_per_beat // 16

# time signature of file (function to recognize later time signature changes)
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

timeSignature = file_stream.getTimeSignatures()[0]
denominator = timeSignature.beatCount
numerator = timeSignature.denominator
ticks_per_measure = get_ticks_per_measure(denominator, numerator)

print("ticks per measure: " + str(ticks_per_measure))
print('time signature {}/{}'.format(denominator, numerator))

# function to mulitply pitch according to duration
def get_pitch_factor(duration):
    pitch_factor = int(duration//thirty_second_ticks)
    return pitch_factor

# function to get thickness of line (amplitude)
def get_y_thickness(msg):
    if 112 <= msg.velocity <= 127:
        y1_thickness = 4
        return y1_thickness

    if 96 <= msg.velocity <= 112:
        y1_thickness = 3.5
        return y1_thickness

    if 80 <= msg.velocity <= 96:
        y1_thickness = 3
        return y1_thickness

    if 64 <= msg.velocity <= 80:
        y1_thickness = 2.5
        return y1_thickness

    if 48 <= msg.velocity <= 64:
        y1_thickness = 1.5
        return y1_thickness

    if 32 <= msg.velocity <= 48:
        y1_thickness = 1
        return y1_thickness

    if 16 <= msg.velocity <= 32:
        y1_thickness = 0.5
        return y1_thickness

    if 0 <= msg.velocity <= 16:
        y1_thickness = 0.1
        return y1_thickness

# --- get line information (pitch, duration, amplitude, measure recognition) --- #
for i, track in enumerate(file_mid.tracks):
    pitch = []
    pitch_d = []
    velocity = []
    velocity_d = []

    for msg in track:
        # get new time signature
        if msg.type == 'time_signature': 
            denominator = msg.denominator
            numerator = msg.numerator
            ticks_per_measure = get_ticks_per_measure(denominator, numerator)
        
        # get list with pitch and duration and velocity of instrument
        if msg.type == "note_on" or msg.type == "note_off":
            pitch.append(msg.note)

            duration = int(msg.time)
            pitch_factor = get_pitch_factor(duration)
            count_pitch_factor = 0
            if msg.time != 0:
                # recognize measure
                count_ticks += msg.time
                if count_ticks >= ticks_per_measure:
                    pitch_d.append("True")
                    count_measures_line += 1
                    count_ticks = 0

                # append pitch with duration
                while count_pitch_factor <= pitch_factor:
                    count_pitch_factor += 1
                    pitch_d.append(int(msg.note))
                    velocity_d.append(get_y_thickness(msg))

            else:
                # recognize measure
                count_ticks += msg.time
                if count_ticks >= ticks_per_measure:
                    pitch_d.append("True")
                    count_ticks = 0

                # append pitch 
                count_ticks += msg.time
                pitch_d.append(int(msg.note))
                velocity_d.append(get_y_thickness(msg))

            velocity.append(msg.velocity)


    # append lists of each instrument to one list (if there's something in the list)
    if pitch and pitch_d and velocity and velocity_d != []:
        all_pitches.append(pitch)
        all_pitches_d.append(pitch_d)
        all_velocities.append(velocity)
        all_velocities_d.append(velocity_d)

# append list with pitch and duration of each instrument to new list
# only the first instrument contains "True" to recognize measures
count_instruments = 0
for instr in all_pitches_d:
    if count_instruments == 0:
        all_pitches_d_m.append(instr)
    else:
        instr_m = list(filter(("True").__ne__, instr))
        all_pitches_d_m.append(instr_m)
    count_instruments += 1

print("--- get line information completed ---")

# --- get plot information (harmony) --- #
def get_color_of_key(key):
    if key == "C major":
        color = "lightsalmon"
        return color

    if key == "G major":
        color = "mediumorchid"
        return color

    if key == "D major":
        color = "dodgerblue "
        return color

    if key == "A major":
        color = "royalblue "
        return color

    if key == "E major":
        color = "turquoise "
        return color

    if key == "B major":
        color = "limegreen "
        return color

    if key == "F# major" or key == "G- major":
        color = "forestgreen"
        return color

    if key == "D- major":
        color = "greenyellow"
        return color

    if key == "A- major":
        color = "gold"
        return color

    if key == "E- major":
        color = "orangered "
        return color

    if key == "B- major":
        color = "lightcoral"
        return color

    if key == "F- major":
        color = "tomato"
        return color

    if key == "a minor":
        color = "darksalmon"
        return color

    if key == "e minor":
        color = "orchid"
        return color

    if key == "b minor":
        color = "crownflowerblue"
        return color

    if key == "f# minor":
        color = "darkblue"
        return color

    if key == "c# minor":
        color = "cadetblue"
        return color

    if key == "g# minor":
        color = "steelblue"
        return color

    if key == "d# minor" or key == "e- minor":
        color = "darkslategrey"
        return color

    if key == "b- minor":
        color = "midnightblue"
        return color

    if key == "f minor":
        color = "goldenrod"
        return color

    if key == "c minor":
        color = "saddlebrown"
        return color

    if key == "g minor":
        color = "sienna"
        return color

    if key == "d minor":
        color = "maroon"
        return color

for track in enumerate(file_mid.tracks):
    count_tracks += 1

allChords = file_stream.chordify()
for c in allChords.getElementsByClass("Measure"):
    k = c.analyze("key")
    keys_per_measure.append(str(k))

for k in keys_per_measure:
    color_per_measure.append(get_color_of_key(k))

print("--- get plot information completed ---")
print(all_velocities_d)
print(all_velocities)
print(color_per_measure)