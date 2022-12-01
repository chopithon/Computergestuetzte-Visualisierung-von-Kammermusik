import mido
from mido import MidiFile
from music21 import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy

# Input-Datei als MidiFile (mido-Bibliothek) und als Stream (music21) lesen
file_path = "midi-files/4_moz-div.mid"
file_mid = MidiFile(file_path)
file_stream = converter.parse(file_path)

# Dreidimensionales Koordinatensystem erstellen
abbildung = plt.figure()
achsen = plt.axes(projection="3d")

# Benötigte Listen und Variablen definieren
all_pitches = []  # Tonhöhe aller Instrumente
all_pitches_d = [] # Tonhöhe aller Instrumente mit der Tondauer
all_pitches_d_m = [] # Tonhöhe aller Instrumente mit der Tondauer pro Takt
all_velocities = [] # Lautstärke aller Instrumente
all_velocities_d = [] # Lautstärke aller Instrumente mit Tondauer
start_values = [] # y-Startpunkt der Linien

keys_per_measure = [] # Tonarten pro Takt
color_per_measure = [] # Farben der Ebene pro Takt
color_i = [] # Index der Tonhöhe, wo die Takterkennungen vorkommen

# count_x sind Variablen, mit welchen Schleifen programmiert werden
count_ticks = 0 # Ticks
count_tracks = 0 # Tracks des MIDI-Files, also die Instrumente
count_thickness_i = 101 # Index der Liste im Array mit allen Dicken der Linien
count_pitch_i = 101 # Index der Liste im Array mit allen Toonhöhen der Linien
count_color_i = 0 # Index der Liste color_i

start_value_i = 0 # Startpunkt der y-Koordinaten 


# --- ALLGEMEINE INFORMATIONEN ÜBER DAS STÜCK --- #
print("--- Allgemeine Informationen ---")

# Tonart des Musikstückes bestimmen
key_file = file_stream.analyze("key")
print("Tonart des Stückes: " + str(key_file))

# Ticks pro Viertel und Sechzehntel bestimmen
ticks_per_beat = file_mid.ticks_per_beat
thirty_second_ticks = file_mid.ticks_per_beat // 16
print("Ticks pro Viertel: " + str(ticks_per_beat))

# Frequenz und Amplitude der Welle bestimmen 
freq = ticks_per_beat / 100
ampl = 3 

# Ticks pro Takt bestimmen
def get_ticks_per_measure(denominator, numerator):
    global ticks_per_beat
    if denominator == 4:
        ticks_per_measure = ticks_per_beat * numerator

    elif denominator == 8:
        ticks_per_beat /= 2 # get ticks per quaver
        ticks_per_measure = ticks_per_beat * numerator

    elif denominator == 16:
        ticks_per_beat /= 4 # get ticks per sixteen
        ticks_per_measure = ticks_per_beat * numerator

    elif denominator == 2:
        ticks_per_beat *= 2 # get ticks per half
        ticks_per_measure = ticks_per_beat * numerator
    
    return ticks_per_measure

# Taktart und Ticks pro Takt bestimmen
timeSignature = file_stream.getTimeSignatures()[0]
denominator = timeSignature.beatCount
numerator = timeSignature.denominator
ticks_per_measure = get_ticks_per_measure(denominator, numerator)

print("Ticks pro Takt: " + str(ticks_per_measure))
print("Taktart: {}/{}".format(denominator, numerator))

# Funktion um zu bestimmen, wie oft die Tonhöhe angehängt werden soll
def get_pitch_factor(duration):
    pitch_factor = int(duration//thirty_second_ticks)
    return pitch_factor

# Funktionen um die Dicke der Linie zu bestimmen. 
# Je nach dem in welchem der folgenden acht Teile die Lautstärke liegt, ist die Linie verschieden dick.  
def get_y_thickness(msg):
    if 112 <= msg.velocity <= 127:
        y1_thickness = 3
        return y1_thickness

    if 96 <= msg.velocity <= 112:
        y1_thickness = 2.75
        return y1_thickness

    if 80 <= msg.velocity <= 96:
        y1_thickness = 2.5
        return y1_thickness

    if 64 <= msg.velocity <= 80:
        y1_thickness = 2.25
        return y1_thickness

    if 48 <= msg.velocity <= 64:
        y1_thickness = 2
        return y1_thickness

    if 32 <= msg.velocity <= 48:
        y1_thickness = 1.75
        return y1_thickness

    if 16 <= msg.velocity <= 32:
        y1_thickness = 1.5
        return y1_thickness

    if 0 <= msg.velocity <= 16:
        y1_thickness = 0.75
        return y1_thickness


# --- INFORMATIONEN ÜBER DIE LINIE (TOONHÖHE, TONDAUER, LAUTSTÄRKE, TAKTERKENNUNG) --- #
for i, track in enumerate(file_mid.tracks):
    pitch = []
    pitch_d = []
    velocity = []
    velocity_d = []

    for msg in track:
        
        # bpm berechnen
        if msg.type == 'set_tempo':
                bpm = mido.tempo2bpm(msg.tempo)
                print(bpm)

                bps = int(bpm * 60) # beats per second
                sixps = bps * 4 # sixteenths per second
                print(sixps)

        # Neue Taktart bestimmen
        if msg.type == 'time_signature': 
            denominator = msg.denominator
            numerator = msg.numerator
            ticks_per_measure = get_ticks_per_measure(denominator, numerator)
        
        # Liste mit Tonhöhe und Liste mit Lautstärke für jedes Instrument erstellen
        # Jedes Element wird je nach dem, wie lange der Ton dauert, mehrfach oder nur einfach hinzugefügt. 
        # Dafür wird berechnet, in welchem Verhältnis die Tondauer zur Dauer einer Sechszehntelnote steht.
        if msg.type == "note_on" or msg.type == "note_off":
            pitch.append(msg.note)

            duration = int(msg.time)
            pitch_factor = get_pitch_factor(duration)
            count_pitch_factor = 0
            if msg.time != 0:

                # Takt erkennen
                count_ticks += msg.time
                if count_ticks >= ticks_per_measure:
                    pitch_d.append("Measure")
                    count_ticks = 0

                # Tonhöhe ("inkl. Tondauer") hinzufügen
                while count_pitch_factor <= pitch_factor:
                    count_pitch_factor += 1
                    pitch_d.append(int(msg.note))
                    velocity_d.append(get_y_thickness(msg))

            else:

                # Takt erkennen
                count_ticks += msg.time
                if count_ticks >= ticks_per_measure:
                    pitch_d.append("Measure")
                    count_ticks = 0

                # Tonhöhe ("inkl. Tondauer") hinzufügen
                count_ticks += msg.time
                pitch_d.append(int(msg.note))
                velocity_d.append(get_y_thickness(msg))

            velocity.append(msg.velocity)


    # Liste mit der Tonhöhe bzw. Lautstärke eines einzelnen Instruments an 
    # Liste mit der Tonhöhe bzw. Lautstärke aller Instrumente hinzufügen.
    if pitch and pitch_d and velocity and velocity_d != []:
        all_pitches.append(pitch)
        all_pitches_d.append(pitch_d)
        all_velocities.append(velocity)
        all_velocities_d.append(velocity_d)

# Liste mit der Tonhöhe aller Instrumente an neue Liste anhängen
# Nun enthält nur noch das erste Instrument die Takterkennung
count_instruments = 0
for instr in all_pitches_d:
    if count_instruments == 0:
        all_pitches_d_m.append(instr)
    else:
        instr_m = list(filter(("Measure").__ne__, instr))
        all_pitches_d_m.append(instr_m)
    count_instruments += 1

# Startpunkt der y-Koordinate jedes Instrumentes berechnen, so dass die Linien gleichmässig über der Ebene verteilt sind.
count = 0
count_instr = len(all_pitches_d_m)
while count <= count_instr:
    start_value = (100/count_instr*count)-50
    start_values.append(start_value)
    count += 1

print("--- get line information completed ---")

# --- INFORMATIONEN ZUR EBENE (HARMONIE) --- #

# Funktion, um die Farbe jeder Tonart zu bestimmen
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

    if key == "F major":
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

# Tonarten pro Takt bestimmen
for track in enumerate(file_mid.tracks):
    count_tracks += 1

allChords = file_stream.chordify()
for c in allChords.getElementsByClass("Measure"):
    k = c.analyze("key")
    keys_per_measure.append(str(k))

# Farbe jeder Tonart bestimmen
for k in keys_per_measure:
    color_per_measure.append(get_color_of_key(k))

print("--- get plot information completed ---")

# Index der Takterkennung des ersten Instrumentes bestimmen.
count_instr = 0
index = 0
for instr in all_pitches_d_m:
    listed = all_pitches_d_m[count_instr]
    if count_instr == 0:
        for i in listed:
            if i == "Measure":
                color_i.append(index)
            index += 1
    count_instr = 1
count_color_i = 0

# --- VISUALISIERUNG --- #
# Basis Komponente der Linie bestimmen x-Achse und ein leeres Array, um die Liste mit den Tonhöhen zu einem Array zu machen.
x1 = numpy.linspace(-50, 50, 100)
zi_array = numpy.full(100, 1)
zj_array = numpy.full(100, 1)
zi_array, zj_array = numpy.meshgrid(zi_array, zj_array)
z_array = zi_array

# Linie zeichnen (Tonhöhe, Tondauer, Lautstärke eines Instrumentes)
def plot_lines(start_value, thickness, z_listed):
    global z_array 

    x1 = numpy.linspace(-50, 50, 100)

    # y-Koordinate des Instruments: die Dicke der Linie des Instruments auf dem jeweiligen Startpunkt
    y1_max = start_value + thickness
    y1_min = start_value - thickness
    y1 = numpy.linspace(y1_max, y1_min, 100)
    x1, y1 = numpy.meshgrid(x1, y1)

    # z-Koordinate des Instruments: Liste mit 100 Tonhöhen als Array
    z1 = z_listed * z_array

    achsen.plot_surface(x1, y1, z1, color = "black")

count_instr = 0

# Eine Linie für jedes Instrument zeichnen
for instr in all_pitches_d_m:

    # Liste mit den ersten Hundert Tonhöhen des Instruments
    pitch_list_m_all = all_pitches_d_m[count_instr]
    pitch_list_m = pitch_list_m_all[:100]

    # Dicke der Linie des letzten Tones aus der Lites mit den Tonhöhen des Instruments
    thickness_list = all_velocities_d[count_instr]
    thickness = thickness_list[count_thickness_i]

    # Die Liste mit den hundert Tonhöhen enthält noch die Takterkennungen, 
    # diese werden nun entfernt und durch die nächste Tonhöhe ersetzt.
    count = 0
    for p in pitch_list_m:
        if p == "Measure":
            key_color = color_per_measure[count_color_i]
            count_color_i += 1

            pitch_list_m.pop(count)
            pitch_list_next = pitch_list_m_all[count_pitch_i]
            pitch_list_m.append(pitch_list_next)
            count_pitch_i += 1
        count += 1

    # Linie zeichnen
    z_listed = pitch_list_m 
    start_value = start_values[start_value_i]
    plot_lines(start_value, thickness, z_listed)

    count_instr += 1
    start_value_i += 1

count_thickness_i += 1
count_instr = 0
start_value_i = 0

# Basis Komponente der Ebene bestimmen
x2 = numpy.linspace(-50, 50, 100)
y2 = numpy.linspace(-50, 50, 100)
x2, y2 = numpy.meshgrid(x2, y2)
z2= numpy.cos(freq*x2* numpy.pi/3)*ampl

# Farbige Ebene zeichnen
graph2 = achsen.plot_surface(x2, y2, z2, color = key_color)

# Achsen regulieren (jede Achse soll gleich lang sein)
achsen.set_zlim(0, 100)
achsen.set_xlim(-50, 50)
achsen.set_ylim(-50, 50)
achsen.set_box_aspect((1, 1, 1))


# ---------- ANIMIERUNG ---------- #

# Funktion um die Ebene und die Linien zu animieren
def schritt(i):
    global count_thickness_i, count_pitch_i, count_color_i, start_values, start_value_i, all_pitches_d_m, all_velocities_d, count_instr, x2, y2, freq, ampl
    achsen.clear()

    count_100 = 0

    
    # Jede Linie neu zeichnen
    for instr in all_pitches_d_m:

            # Neue Dicke der Linie bestimmen
            thickness_list = all_velocities_d[count_instr]
            thickness = thickness_list[count_thickness_i]

            # Neue Tonhöhe bestimmen, in dem die nächsten 100 Elemente berechnet werden
            # (Gleiche Berechnung wie beim ersten Zeichnen, nur werden jeweils die nächsten 100 Elemente der Tonhöhe bzw. die nächste Dicke verwendet)
            pitch_100 = []
            pitch_list = all_pitches_d_m[count_instr] 
            count_pitches_100 = count_thickness_i 

            if count_instr == 0:
                count_pitches_100 = count_pitch_i
                while count_100 < 100:
                    count_100 += 1
                    count_pitches_100 += 1
                    new_pitch = pitch_list[count_pitches_100]
                    if new_pitch == "Measure":
                        count_100 -= 1
                    else:
                        pitch_100.append(new_pitch)

            else:
                while count_100 < 100:
                    count_100 += 1
                    count_pitches_100 += 1
                    pitch_100.append(pitch_list[count_pitches_100])
            
            if count_pitch_i == color_i[count_color_i]:
                key_color = color_per_measure[count_color_i]
                count_color_i += 1
            print(color_i[count_color_i])
            print(count_pitch_i)

            start_value = start_values[start_value_i]
            
            plot_lines(start_value, thickness, pitch_100)

            count_100 = 0
            count_instr += 1
            start_value_i += 1    
        
    
    count_thickness_i += 1
    count_pitch_i += 1
    count_instr = 0
    start_value_i = 0

    # Neue Ebene zeichnen
    z2 = numpy.cos((freq*x2 + 1*i)* numpy.pi/3)*ampl
    key_color = color_per_measure[count_color_i]
    achsen.plot_surface(x2, y2, z2, color = key_color)

    # Achsen wieder regulieren
    achsen.set_zlim(0, 100)
    achsen.set_xlim(-50, 50)
    achsen.set_ylim(-50, 50)
    achsen.set_box_aspect((1, 1, 1))

# Linien und die Ebene visualisieren.
animation = FuncAnimation(abbildung, schritt, frames = bps, interval = 20, blit = False)

animation.save('Visualisierung.gif')

plt.close()