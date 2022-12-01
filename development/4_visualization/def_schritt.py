import mido
from mido import MidiFile
from music21 import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy

# file as MIDI and MIDI-Stream
file_mid = MidiFile("bth-str-trio.mid")
file_stream = converter.parse("bth-str-trio.mid")

# base components of visualization
abbildung = plt.figure()
achsen = plt.axes(projection="3d")

# lists and variables for the music analysis and visualization
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

start_value = -40
count_thickness_i = 101
count_pitch_i = 101
count_color_i = 0

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
print('time signature: {}/{}'.format(denominator, numerator))

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
        color = "dodgerblue"
        return color

    if key == "A major":
        color = "royalblue"
        return color

    if key == "E major":
        color = "turquoise"
        return color

    if key == "B major":
        color = "limegreen"
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
        color = "orangered"
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

# --- visualization --- #
# base components of the lines
x1 = numpy.linspace(-50, 50, 100)
zi_array = numpy.full(100, 1)
zj_array = numpy.full(100, 1)
zi_array, zj_array = numpy.meshgrid(zi_array, zj_array)
z_array = zi_array

# plot a line (pitch, duration, velocity of instrument)
def plot_lines(start_value, thickness, z_listed):
    global z_array 

    x1 = numpy.linspace(-50, 50, 100)
    y1_max = start_value + thickness
    y1_min = start_value - thickness
    y1 = numpy.linspace(y1_max, y1_min, 100)

    x1, y1 = numpy.meshgrid(x1, y1)
    z1 = z_listed * z_array

    achsen.plot_surface(x1, y1, z1, color = "black")

count_instr = 0

# plot a line for each instrument
for instr in all_pitches_d_m:
    thickness_list = all_velocities_d[count_instr]
    thickness = thickness_list[count_thickness_i]

    pitch_list_m_all = all_pitches_d_m[count_instr]
    pitch_list_m = pitch_list_m_all[:100]

    count = 0
    for p in pitch_list_m:
        if p == "True":
            key_color = color_per_measure[count_color_i]
            count_color_i += 1

            pitch_list_m.pop(count)
            pitch_list_next = pitch_list_m_all[count_pitch_i]
            pitch_list_m.append(pitch_list_next)
            count_pitch_i += 1
        count += 1

    z_listed = pitch_list_m 

    plot_lines(start_value, thickness, z_listed)

    count_instr += 1
    start_value += 20

count_thickness_i += 1
count_instr = 0
start_value = 0

# plot the plot
freq = 5.2 
ampl = 3 

x2 = numpy.linspace(-50, 50, 100)
y2 = numpy.linspace(-50, 50, 100)
x2, y2 = numpy.meshgrid(x2, y2)

z2= numpy.cos(freq*x2* numpy.pi/3)*ampl
graph2 = achsen.plot_surface(x2, y2, z2, color = key_color)

achsen.set_zlim(0, 100)
achsen.set_xlim(-50, 50)
achsen.set_ylim(-50, 50)
achsen.set_box_aspect((1, 1, 1))

# --- visualization --- #
def schritt(i):
    global count_thickness_i, count_pitch_i, count_color_i, start_value, all_pitches_d_m, all_velocities_d
    achsen.clear() 

    count_1 = 0 # count instr No. I
    count_100 = 0 # count 100 elements
    pitches_100 = []
    count_instr = 0

    # update lines 
    for instr in all_pitches_d_m:
        # get new pitch list for each instr und update colora
        pitch_100 = []
        count_pitches_100 = count_thickness_i
        pitch_list = all_pitches_d_m[count_instr]
        if count_1 == 0:
            count_pitches_100 = count_pitch_i
            while count_100 < 100:
                count_100 += 1
                count_pitches_100 += 1
                new_pitch = pitch_list[count_pitches_100]
                if new_pitch == "True":
                    key_color = color_per_measure[count_color_i]
                    count_color_i += 1
                    count_100 -= 1
                else:
                    pitch_100.append(new_pitch)        
            count_1 = 1
        else:
            print(pitch_list)
            count_pitches_100 = count_thickness_i
            while count_100 < 100:
                count_100 += 1
                count_pitches_100 += 1
                pitch_100.append(pitch_list[count_pitches_100])
        count_100 = 0

        # get new thickness
        thickness_list = all_velocities_d[count_instr]
        thickness = thickness_list[count_thickness_i]

        # plot new line for each instr
        plot_lines(start_value, thickness, pitch_100)

        count_instr += 1
        start_value += 20


    count_thickness_i += 1
    count_pitch_i += 1
    count_instr = 0
    start_value = 0

    # update plot
    freq = 5.2 
    ampl = 3 

    x2 = numpy.linspace(-50, 50, 100)
    y2 = numpy.linspace(-50, 50, 100)
    x2, y2 = numpy.meshgrid(x2, y2)

    z2= numpy.cos(freq*x2* numpy.pi/3)*ampl
    achsen.plot_surface(x2, y2, z2, color = key_color)

    # update axes
    achsen.set_zlim(0, 100)
    achsen.set_xlim(-50, 50)
    achsen.set_ylim(-50, 50)
    achsen.set_box_aspect((1, 1, 1))


animation = FuncAnimation(abbildung, schritt, interval = 20, blit = False)

plt.show()