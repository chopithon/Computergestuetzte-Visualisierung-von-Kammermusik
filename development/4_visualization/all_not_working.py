import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mido import MidiFile
import mido
from music21 import *
import numpy

file_mid = MidiFile("bth-str-trio.mid")
file_stream = converter.parse("bth-trio.mid")

key_file = file_stream.analyze("key")
ticks_per_beat = file_mid.ticks_per_beat
thirty_second_ticks = file_mid.ticks_per_beat // 16
plot_freq = 5.2
plot_ampl = 3
measure_100 = 0

count_tracks = 0
count_ticks = 0
count_measures = 0
count_plotlines = 0
count_lenz = 100
z1_pitches = []
z2_pitches = []
z3_pitches = []
z1_velocities = []
z2_velocities = []
z3_velocities = []

keys_per_measure = []
colors_per_measure = []
keys_per_measure = []
all_pitches = []
all_velocities = []
plot_pitches = []
plot_velocities = []
all_startvalues = []

def get_color_of_key(key):
    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

    if key == "":
        color = ""
        return color

def get_pitch_factor(duration):
    pitch_factor = int(duration//thirty_second_ticks)
    return pitch_factor

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

abbildung = plt.figure()
achsen = plt.axes(projection="3d")

x1 = numpy.linspace(-50, 50, 100)
zi_array = numpy.full(100, 1)
zj_array = numpy.full(100, 1)
zi_array, zj_array = numpy.meshgrid(zi_array, zj_array)
z_array = zi_array

def plot_lines(z_all, y_all, start_value):
    x1 = numpy.linspace(-50, 50, 100)
    thickness = y_all[100]
    y1_max = start_value + thickness
    y1_min = start_value - thickness
    y1 = numpy.linspace(y1_max, y1_min, 100)
    plot_velocities.append(y1)

    x1, y1 = numpy.meshgrid(x1, y1)
    zi_array = numpy.full(100, 1)
    zj_array = numpy.full(100, 1)
    zi_array, zj_array = numpy.meshgrid(zi_array, zj_array)
    z_array = zi_array
    z1 = z_all[:100] * z_array
    z1 = numpy.cos(5.2*x1* numpy.pi/3)*3
    plot_pitches.append(z1)

    achsen.plot_surface(x1, y1, z1, color = "black")

# --- harmonies ---
for track in enumerate(file_mid.tracks):
    count_tracks += 1

allChords = file_stream.chordify()
for c in allChords.getElementsByClass("Measure"):
    k = c.analyze("key")
    keys_per_measure.append(str(k))

for k in keys_per_measure:
    colors_per_measure.append(get_color_of_key(k))
print("harmonies are analysed")

timeSignature = file_stream.getTimeSignatures()[0]
denominator = timeSignature.beatCount
numerator = timeSignature.denominator
ticks_per_measure = get_ticks_per_measure(denominator, numerator)

# --- pitch, velocity, duration ---
for msg in file_mid:
    if count_tracks == 3:
        z1_pitches = []
        z2_pitches = []
        z3_pitches = []

        z1_velocities = []
        z2_velocities = []
        z3_veocities = []

        y1_startvalue = -40
        y2_startvalue = -20
        y3_startvalue = 0

    if msg.type == 'time_signature': #put timesignatures
        denominator = msg.denominator
        numerator = msg.numerator
        ticks_per_measure = get_ticks_per_measure(denominator, numerator)

    elif msg.type == "note_on" or msg.type == "note.off":
        if msg.channel == 0:
            duration = int(msg.time)
            pitch_factor = get_pitch_factor(duration)
            count_pitch_factor = 0
            while count_pitch_factor <= pitch_factor:
                count_pitch_factor += msg.note
                z1_pitches.append(msg.note)
                if len(z1_pitches) == 100:
                    measure_100 = count_measures

                count_ticks += msg.time
                if count_ticks >= ticks_per_measure:
                    z1_pitches.append("True")
                    count_ticks = 0

                z1_velocities.append(get_y_thickness(msg))
                print("Note appended 0")


        elif msg.channel == 1:
            duration = int(msg.time)
            pitch_factor = get_pitch_factor(duration)
            count_pitch_factor = 0
            while count_pitch_factor <= pitch_factor:
                count_pitch_factor += msg.note
                z2_pitches.append(msg.note)
                print("Note appended 1")

        elif msg.channel == 2:
            duration = int(msg.time)
            pitch_factor = get_pitch_factor(duration)
            count_pitch_factor = 0
            while count_pitch_factor <= pitch_factor:
                count_pitch_factor += msg.note
                z3_pitches.append(msg.note)
                print("Note appended 2")

print(z1_pitches)
if count_tracks == 3:
    all_pitches.append(z1_pitches)
    all_pitches.append(z2_pitches)
    all_velocities.append(z1_velocities)
    all_velocities.append(z2_velocities)

"""
for instr in all_pitches:
    plot_lines(instr, all_velocities[count_plotlines], all_startvalues[count_plotlines])
    count_plotlines += 1
"""

print(count_tracks)
print(all_pitches)
print(all_velocities)
print(keys_per_measure)

#plt.show()


"""
def create_z_lists(count_tracks):
    if count_tracks == 0:
        print("no tracks in MIDI-file!")

    elif count_tracks == 1:
        print("only one track!")

    elif count_tracks == 2:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []

    elif count_tracks == 3:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []

    elif count_tracks == 4:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []

    elif count_tracks == 5:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []

    elif count_tracks == 6:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []

    elif count_tracks == 7:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []

    elif count_tracks == 8:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []

    elif count_tracks == 9:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []
        z9_pitch = []
        z9_velocity = []

    elif count_tracks == 10:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []
        z9_pitch = []
        z9_velocity = []
        z10_pitch = []
        z10_velocity = []

    elif count_tracks == 11:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []
        z9_pitch = []
        z9_velocity = []
        z10_pitch = []
        z10_velocity = []
        z11_pitch = []
        z11_velocity = []

    elif count_tracks == 12:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []
        z9_pitch = []
        z9_velocity = []
        z10_pitch = []
        z10_velocity = []
        z11_pitch = []
        z11_velocity = []
        z12_pitch = []
        z12_velocity = []

    elif count_tracks == 13:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []
        z9_pitch = []
        z9_velocity = []
        z10_pitch = []
        z10_velocity = []
        z11_pitch = []
        z11_velocity = []
        z12_pitch = []
        z12_velocity = []
        z13_pitch = []
        z13_velocity = []

    elif count_tracks == 14:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []
        z9_pitch = []
        z9_velocity = []
        z10_pitch = []
        z10_velocity = []
        z11_pitch = []
        z11_velocity = []
        z12_pitch = []
        z12_velocity = []
        z13_pitch = []
        z13_velocity = []
        z14_pitch = []
        z14_velocity = []

    elif count_tracks == 15:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []
        z9_pitch = []
        z9_velocity = []
        z10_pitch = []
        z10_velocity = []
        z11_pitch = []
        z11_velocity = []
        z12_pitch = []
        z12_velocity = []
        z13_pitch = []
        z13_velocity = []
        z14_pitch = []
        z14_velocity = []
        z15_pitch = []
        z15_velocity = []

    elif count_tracks == 16:
        z1_pitch = []
        z1_velocity = []
        z2_pitch = []
        z2_velocity = []
        z3_pitch = []
        z3_velocity = []
        z4_pitch = []
        z4_velocity = []
        z5_pitch = []
        z5_velocity = []
        z6_pitch = []
        z6_velocity = []
        z7_pitch = []
        z7_velocity = []
        z8_pitch = []
        z8_velocity = []
        z9_pitch = []
        z9_velocity = []
        z10_pitch = []
        z10_velocity = []
        z11_pitch = []
        z11_velocity = []
        z12_pitch = []
        z12_velocity = []
        z13_pitch = []
        z13_velocity = []
        z14_pitch = []
        z14_velocity = []
        z15_pitch = []
        z15_velocity = []
        z16_pitch = []
        z16_velocity = []

def update_ax(list, all_list, counter, color):
    listed = list.tolist()

    for k in listed:
        k.pop(0)
        k.append(all_list[counter])

    new_list = numpy.array(listed)
    
    return new_list

thirty_second_ticks = mid.ticks_per_beat
pitch_factor = int(msg.duration//thirty_second_ticks)
"""