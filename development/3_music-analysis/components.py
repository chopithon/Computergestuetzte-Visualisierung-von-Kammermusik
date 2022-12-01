from music21 import converter,instrument # or import *

file = converter.parse('vns_rnd.mid')
components = []
str_components = []

for element in file.recurse():
    components.append(element)

print(len(components))
"""
for i in components:
    print(str(i))

i = 0
while i < 400:
    print(components[i])
    i += 1
"""


# output
"""
<music21.stream.Part 0x104909e10>
<music21.stream.Measure 1 offset=0.0>
Violin: Violin
<music21.clef.TrebleClef>
<music21.tempo.MetronomeMark Quarter=100.0>
G major
<music21.meter.TimeSignature 3/4>
<music21.note.Rest dotted-half>
<music21.stream.Measure 2 offset=3.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 3 offset=6.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 4 offset=9.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 5 offset=12.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 6 offset=15.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 7 offset=18.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 8 offset=21.0>
<music21.note.Rest quarter>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Rest quarter>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Rest quarter>
<music21.stream.Measure 9 offset=24.0>
<music21.note.Rest dotted-quarter>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note D>
<music21.stream.Measure 10 offset=27.0>
<music21.note.Note D>
<music21.note.Note G>
<music21.stream.Measure 11 offset=30.0>
<music21.note.Note G>
<music21.note.Note F#>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.stream.Measure 12 offset=33.0>
<music21.note.Note D>
<music21.note.Note G>
<music21.stream.Measure 13 offset=36.0>
<music21.note.Note G>
<music21.note.Note F#>
<music21.note.Note E>
<music21.note.Note D>
<music21.note.Note C#>
<music21.note.Note E>
<music21.stream.Measure 14 offset=39.0>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note D>
<music21.note.Rest 16th>
<music21.note.Note C>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.stream.Measure 15 offset=42.0>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Note D>
<music21.note.Rest 16th>
<music21.note.Note C>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Note D>
<music21.stream.Measure 16 offset=45.0>
<music21.note.Note C>
<music21.note.Rest 16th>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note B>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Note C>
<music21.stream.Measure 17 offset=48.0>
<music21.note.Note D>
<music21.note.Note E>
<music21.note.Note F#>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Note G>
<music21.stream.Measure 18 offset=51.0>
<music21.note.Note F#>
<music21.note.Note D>
<music21.note.Note A>
<music21.note.Note G>
<music21.note.Note F#>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note D>
<music21.note.Note A>
<music21.note.Note G>
<music21.stream.Measure 19 offset=54.0>
<music21.note.Note G>
<music21.note.Note F#>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.note.Note E>
<music21.note.Note D>
<music21.tempo.MetronomeMark maestoso Quarter=88.0>
<music21.note.Note C#>
<music21.note.Note C>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Note D>
<music21.stream.Measure 20 offset=57.0>
<music21.note.Note C>
<music21.note.Rest 16th>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note B>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Note C>
<music21.stream.Measure 21 offset=60.0>
<music21.note.Note D>
<music21.note.Note E>
<music21.note.Note F#>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Note G>
<music21.stream.Measure 22 offset=63.0>
<music21.note.Note F#>
<music21.note.Note E>
<music21.note.Note A>
<music21.note.Note G>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note F#>
<music21.note.Note E>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Note F#>
<music21.note.Rest 16th>
<music21.stream.Measure 23 offset=66.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note G>
<music21.note.Note D>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.stream.Measure 24 offset=69.0>
<music21.stream.Voice 0x102a3c1c0>
<music21.note.Note G>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.note.Note G>
<music21.note.Note A>
<music21.stream.Voice 0x102a0ae90>
<music21.note.Rest dotted-quarter>
<music21.note.Note A>
<music21.note.Rest quarter>
<music21.stream.Measure 25 offset=72.0>
<music21.note.Note B->
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note C>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.stream.Measure 26 offset=75.0>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note F#>
<music21.note.Rest 16th>
<music21.stream.Measure 27 offset=78.0>
<music21.note.Note F#>
<music21.note.Rest eighth>
<music21.note.Note F#>
<music21.note.Note C>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.stream.Measure 28 offset=81.0>
<music21.stream.Voice 0x1049b6ef0>
<music21.note.Note F#>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note F#>
<music21.note.Rest 16th>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.stream.Voice 0x1049b7280>
<music21.note.Rest dotted-quarter>
<music21.note.Note G>
<music21.note.Rest quarter>
<music21.stream.Measure 29 offset=84.0>
<music21.note.Note G#>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note E>
<music21.note.Rest 16th>
<music21.note.Note C>
<music21.note.Rest 16th>
<music21.stream.Measure 30 offset=87.0>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note D>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Rest 16th>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.note.Note D>
<music21.note.Rest 16th>
<music21.stream.Measure 31 offset=90.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note F#>
<music21.note.Rest 16th>
<music21.stream.Measure 32 offset=93.0>
<music21.note.Note F#>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.note.Note E>
<music21.note.Rest 16th>
<music21.note.Note E>
<music21.note.Note E->
<music21.note.Rest 16th>
<music21.note.Note F#>
<music21.note.Rest 16th>
<music21.stream.Measure 33 offset=96.0>
<music21.note.Note F#>
<music21.note.Note E>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.stream.Measure 34 offset=99.0>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note F#>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.stream.Measure 35 offset=102.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note A>
<music21.note.Note G#>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.stream.Measure 36 offset=105.0>
<music21.note.Note B>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.note.Note C#>
<music21.note.Rest 16th>
<music21.note.Note C#>
<music21.note.Rest 16th>
<music21.stream.Measure 37 offset=108.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note A>
<music21.note.Note G#>
<music21.note.Note B>
<music21.note.Note A>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note C#>
<music21.note.Note B>
<music21.stream.Measure 38 offset=111.0>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.note.Note C#>
<music21.note.Rest 16th>
<music21.stream.Measure 39 offset=114.0>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note D>
<music21.note.Note C#>
<music21.note.Note E>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Measure 40 offset=117.0>
<music21.note.Note E>
<music21.note.Note E->
<music21.note.Note F#>
<music21.note.Note E>
<music21.note.Rest eighth>
<music21.stream.Measure 41 offset=120.0>
<music21.note.Note E>
<music21.note.Note F#>
<music21.note.Rest 16th>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.note.Note A>
<music21.note.Rest 16th>
<music21.note.Note B>
<music21.note.Rest 16th>
<music21.stream.Measure 42 offset=123.0>
<music21.note.Note A>
<music21.note.Note F#>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note A>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.note.Rest eighth>
<music21.stream.Measure 43 offset=126.0>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note D>
<music21.note.Rest half>
<music21.stream.Measure 44 offset=129.0>
<music21.note.Note C#>
<music21.note.Rest half>
<music21.stream.Measure 45 offset=132.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.chord.Chord G3 C#4>
<music21.chord.Chord G3 C#4>
<music21.chord.Chord G3 C#4>
<music21.stream.Measure 46 offset=135.0>
<music21.chord.Chord F#3 D4>
<music21.note.Rest eighth>
<music21.chord.Chord G3 C#4>
<music21.note.Rest eighth>
<music21.stream.Measure 47 offset=138.0>
<music21.chord.Chord F#3 D4>
<music21.note.Rest eighth>
<music21.chord.Chord G3 C#4>
<music21.note.Rest eighth>
<music21.stream.Measure 48 offset=141.0>
<music21.chord.Chord F#3 D4>
<music21.note.Rest half>
<music21.stream.Measure 49 offset=144.0>
<music21.chord.Chord E3 D4>
<music21.note.Rest eighth>
<music21.chord.Chord C#4 A3>
<music21.note.Rest eighth>
<music21.stream.Measure 50 offset=147.0>
<music21.chord.Chord D4 D3>
<music21.note.Rest half>
<music21.stream.Measure 51 offset=150.0>
<music21.chord.Chord D4 E3>
<music21.note.Rest eighth>
<music21.chord.Chord C#4 A3>
<music21.note.Rest eighth>
<music21.stream.Measure 52 offset=153.0>
<music21.chord.Chord B3 D4>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Note B>
<music21.note.Note E>
<music21.stream.Measure 53 offset=156.0>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note F#>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Note E>
<music21.stream.Measure 54 offset=159.0>
<music21.note.Note F#>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note G>
<music21.note.Note B>
<music21.note.Note E>
<music21.stream.Measure 55 offset=162.0>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note F#>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note A>
<music21.note.Note C#>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.note.Note E>
<music21.stream.Measure 56 offset=165.0>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.chord.Chord D3 D4>
<music21.note.Rest quarter>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark maestoso Quarter=88.0>
<music21.note.Rest eighth>
<music21.stream.Measure 57 offset=168.0>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.note.Note D>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note F#>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note F#>
<music21.note.Note A>
<music21.stream.Measure 58 offset=171.0>
<music21.note.Note D>
<music21.note.Rest 2.5ql>
<music21.stream.Measure 59 offset=174.0>
<music21.note.Rest quarter>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark andantino Quarter=80.0>
<music21.note.Rest quarter>
<music21.stream.Measure 60 offset=177.0>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.stream.Voice 0x102fa2bc0>
<music21.note.Rest dotted-quarter>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Voice 0x102fa2e00>
<music21.note.Rest 1.75ql>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 61 offset=180.0>
<music21.stream.Voice 0x102fa3070>
<music21.note.Note A>
<music21.note.Note A>
<music21.note.Note A>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.stream.Voice 0x102fa3400>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 62 offset=183.0>
<music21.stream.Voice 0x102fa3820>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.stream.Voice 0x102fa3bb0>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 63 offset=186.0>
<music21.stream.Voice 0x102fa3fd0>
<music21.note.Note C>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Note C>
<music21.note.Note A>
<music21.note.Note B>
<music21.stream.Voice 0x10300c3a0>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 64 offset=189.0>
<music21.stream.Voice 0x10300c7c0>
<music21.note.Note C>
<music21.note.Rest quarter>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Voice 0x10300ca90>
<music21.note.Rest 1.75ql>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 65 offset=192.0>
<music21.stream.Voice 0x10300cd00>
<music21.note.Note A>
<music21.note.Note A>
<music21.note.Note A>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.stream.Voice 0x10300d090>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 66 offset=195.0>
<music21.stream.Voice 0x10300d4b0>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.chord.Chord G4 B4>
<music21.chord.Chord G4 B4>
<music21.chord.Chord G4 B4>
<music21.stream.Voice 0x10300da80>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 67 offset=198.0>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.stream.Voice 0x10300df00>
<music21.chord.Chord C5 A4>
<music21.chord.Chord A4 C5>
<music21.chord.Chord G4 B4>
<music21.chord.Chord A4 C5>
<music21.chord.Chord A4 C5>
<music21.chord.Chord A4 C5>
<music21.stream.Voice 0x10300e710>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.tempo.MetronomeMark maestoso Quarter=88.0>
<music21.stream.Measure 68 offset=201.0>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.chord.Chord B4 G4>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.stream.Measure 69 offset=204.0>
<music21.note.Note F#>
<music21.note.Rest eighth>
<music21.note.Note C#>
<music21.note.Rest eighth>
<music21.stream.Measure 70 offset=207.0>
<music21.stream.Voice 0x10300f1f0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.stream.Voice 0x10300f4c0>
<music21.note.Rest 1.75ql>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.stream.Measure 71 offset=210.0>
<music21.stream.Voice 0x10300f700>
<music21.note.Note D>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.stream.Voice 0x10300f9d0>
<music21.note.Rest 16th>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Rest 1.75ql>
<music21.stream.Measure 72 offset=213.0>
<music21.note.Note D>
<music21.note.Rest half>
<music21.stream.Measure 73 offset=216.0>
<music21.tempo.MetronomeMark Quarter=98.0>
<music21.note.Rest dotted-quarter>
<music21.tempo.MetronomeMark moderate Quarter=94.0>
<music21.note.Rest dotted-quarter>
<music21.stream.Measure 74 offset=219.0>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Rest dotted-quarter>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Measure 75 offset=222.0>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note C>
<music21.note.Note C>
<music21.note.Note C>
<music21.stream.Measure 76 offset=225.0>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Measure 77 offset=228.0>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.stream.Measure 78 offset=231.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Measure 79 offset=234.0>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note C>
<music21.note.Note C>
<music21.note.Note C>
<music21.stream.Measure 80 offset=237.0>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Measure 81 offset=240.0>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.stream.Measure 82 offset=243.0>
<music21.stream.Voice 0x103075a50>
<music21.note.Note G>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note B->
<music21.note.Note C>
<music21.note.Note B->
<music21.note.Note A>
<music21.note.Note G>
<music21.stream.Voice 0x103075f00>
<music21.note.Rest dotted-eighth>
<music21.note.Note E->
<music21.note.Rest half>
<music21.stream.Measure 83 offset=246.0>
g minor
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Measure 84 offset=249.0>
<music21.note.Note B->
<music21.note.Rest eighth>
<music21.note.Note F#>
<music21.note.Rest eighth>
<music21.stream.Measure 85 offset=252.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.stream.Measure 86 offset=255.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.stream.Measure 87 offset=258.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Measure 88 offset=261.0>
<music21.note.Note B->
<music21.note.Rest eighth>
<music21.note.Note F#>
<music21.note.Rest eighth>
<music21.stream.Measure 89 offset=264.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.stream.Measure 90 offset=267.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.stream.Measure 91 offset=270.0>
<music21.stream.Voice 0x1030779d0>
<music21.note.Note B->
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note E->
<music21.note.Note E->
<music21.stream.Voice 0x103077d60>
<music21.note.Rest 16th>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.stream.Measure 92 offset=273.0>
<music21.stream.Voice 0x1030d01c0>
<music21.note.Note B->
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note B->
<music21.note.Note C>
<music21.note.Note C>
<music21.stream.Voice 0x1030d0550>
<music21.note.Rest 16th>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.stream.Measure 93 offset=276.0>
<music21.stream.Voice 0x1030d0970>
<music21.note.Note B->
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note E->
<music21.note.Note E->
<music21.stream.Voice 0x1030d0d00>
<music21.note.Rest 16th>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.stream.Measure 94 offset=279.0>
<music21.stream.Voice 0x1030d1120>
<music21.note.Note B->
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note A>
<music21.note.Note C>
<music21.note.Rest eighth>
<music21.stream.Voice 0x1030d1480>
<music21.note.Rest 16th>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note D>
<music21.note.Rest dotted-eighth>
<music21.stream.Measure 95 offset=282.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Measure 96 offset=285.0>
<music21.note.Note B->
<music21.note.Rest eighth>
<music21.note.Note F#>
<music21.note.Rest eighth>
<music21.stream.Measure 97 offset=288.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.stream.Measure 98 offset=291.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.stream.Measure 99 offset=294.0>
<music21.stream.Voice 0x1030d2020>
<music21.note.Note B->
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note E->
<music21.note.Note E->
<music21.stream.Voice 0x1030d23b0>
<music21.note.Rest 16th>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.stream.Measure 100 offset=297.0>
<music21.stream.Voice 0x1030d27d0>
<music21.note.Note B->
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note B->
<music21.note.Note C>
<music21.note.Note C>
<music21.stream.Voice 0x1030d2b60>
<music21.note.Rest 16th>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.stream.Measure 101 offset=300.0>
<music21.stream.Voice 0x1030d2f80>
<music21.note.Note B->
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note E->
<music21.note.Note E->
<music21.stream.Voice 0x1030d3310>
<music21.note.Rest 16th>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.stream.Measure 102 offset=303.0>
<music21.stream.Voice 0x1030d3730>
<music21.note.Note B->
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note A>
<music21.note.Note C>
<music21.note.Rest eighth>
<music21.stream.Voice 0x1030d3a90>
<music21.note.Rest 16th>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note F>
<music21.note.Note D>
<music21.note.Rest dotted-eighth>
<music21.stream.Measure 103 offset=306.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Measure 104 offset=309.0>
<music21.note.Note B->
<music21.note.Rest eighth>
<music21.note.Note F#>
<music21.note.Rest eighth>
<music21.stream.Measure 105 offset=312.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note A>
<music21.tempo.MetronomeMark moderate Quarter=92.0>
<music21.note.Rest eighth>
<music21.stream.Measure 106 offset=315.0>
<music21.tempo.MetronomeMark maestoso Quarter=88.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.stream.Measure 107 offset=318.0>
<music21.tempo.MetronomeMark andantino Quarter=80.0>
<music21.stream.Voice 0x103138910>
<music21.chord.Chord G3 B-3>
<music21.note.Rest dotted-quarter>
<music21.stream.Voice 0x103138af0>
<music21.note.Rest quarter>
<music21.chord.Chord A3 C4>
<music21.note.Rest quarter>
<music21.stream.Measure 108 offset=321.0>
<music21.chord.Chord A3 C4>
<music21.stream.Measure 109 offset=328.0>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.chord.Chord A3 C4>
<music21.stream.Measure 110 offset=332.0>
<music21.chord.Chord A3 C4>
<music21.note.Rest half>
<music21.stream.Measure 111 offset=335.0>
<music21.note.Rest dotted-quarter>
<music21.chord.Chord G3 D4>
<music21.note.Rest eighth>
<music21.stream.Measure 112 offset=338.0>
<music21.note.Rest quarter>
<music21.note.Note C#>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Measure 113 offset=341.0>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 114 offset=344.0>
<music21.note.Note D>
<music21.note.Note D>
<music21.tempo.MetronomeMark Quarter=98.0>
<music21.note.Note D>
<music21.note.Note D>
<music21.tempo.MetronomeMark moderate Quarter=94.0>
<music21.note.Note D>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Note D>
<music21.stream.Measure 115 offset=347.0>
<music21.tempo.MetronomeMark Quarter=100.0>
G major
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.chord.Chord G3 D4>
<music21.note.Rest eighth>
<music21.stream.Measure 116 offset=350.0>
<music21.note.Rest quarter>
<music21.note.Note C#>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Measure 117 offset=353.0>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 118 offset=356.0>
<music21.chord.Chord C4 D3>
<music21.chord.Chord C4 D3>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.chord.Chord C4 D3>
<music21.chord.Chord C4 D3>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.chord.Chord C4 D3>
<music21.tempo.MetronomeMark andantino Quarter=80.0>
<music21.chord.Chord C4 D3>
<music21.stream.Measure 119 offset=359.0>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note D>
<music21.note.Note F#>
<music21.note.Note A>
<music21.stream.Measure 120 offset=362.0>
<music21.note.Note C>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 121 offset=365.0>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 122 offset=368.0>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.stream.Measure 123 offset=371.0>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note D>
<music21.stream.Measure 124 offset=374.0>
<music21.stream.Voice 0x103199060>
<music21.chord.Chord A3 D4>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Voice 0x1031993f0>
<music21.note.Rest 1.75ql>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 125 offset=377.0>
<music21.stream.Voice 0x103199660>
<music21.note.Note A>
<music21.note.Note A>
<music21.note.Note A>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.stream.Voice 0x1031999f0>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 126 offset=380.0>
<music21.stream.Voice 0x103199e10>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.chord.Chord G4 B4>
<music21.chord.Chord G4 B4>
<music21.chord.Chord G4 B4>
<music21.stream.Voice 0x10319a3e0>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.stream.Measure 127 offset=383.0>
<music21.stream.Voice 0x10319a800>
<music21.chord.Chord C5 A4>
<music21.chord.Chord A4 C5>
<music21.chord.Chord G4 B4>
<music21.chord.Chord A4 C5>
<music21.chord.Chord A4 C5>
<music21.chord.Chord A4 C5>
<music21.stream.Voice 0x10319b010>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note D>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.stream.Measure 128 offset=386.0>
<music21.chord.Chord B4 G4>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.stream.Measure 129 offset=389.0>
<music21.note.Note F#>
<music21.note.Rest eighth>
<music21.note.Note C#>
<music21.note.Rest eighth>
<music21.stream.Measure 130 offset=392.0>
<music21.stream.Voice 0x10319ba90>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.stream.Voice 0x10319bd60>
<music21.note.Rest 1.75ql>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Rest 16th>
<music21.stream.Measure 131 offset=395.0>
<music21.stream.Voice 0x10319bfa0>
<music21.note.Note D>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.stream.Voice 0x1031fc2b0>
<music21.note.Rest 16th>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Rest 1.75ql>
<music21.stream.Measure 132 offset=398.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note C>
<music21.note.Rest eighth>
<music21.stream.Measure 133 offset=401.0>
<music21.note.Note B>
<music21.note.Rest eighth>
<music21.note.Note F#>
<music21.stream.Measure 134 offset=404.0>
<music21.stream.Voice 0x1031fc8b0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note C>
<music21.note.Note G>
<music21.note.Note C>
<music21.stream.Voice 0x1031fcb80>
<music21.note.Rest 1.75ql>
<music21.note.Note E>
<music21.note.Note E>
<music21.note.Rest 16th>
<music21.stream.Measure 135 offset=407.0>
<music21.stream.Voice 0x1031fcdc0>
<music21.note.Note B>
<music21.note.Note G>
<music21.note.Note B>
<music21.note.Note F#>
<music21.note.Rest eighth>
<music21.stream.Voice 0x1031fd090>
<music21.note.Rest 16th>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Rest 1.75ql>
<music21.stream.Measure 136 offset=410.0>
<music21.note.Note G>
<music21.note.Rest half>
<music21.stream.Measure 137 offset=413.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 138 offset=416.0>
<music21.note.Rest dotted-quarter>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Note G>
<music21.stream.Measure 139 offset=419.0>
<music21.note.Note G#>
<music21.note.Note A>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note G>
<music21.note.Note B>
<music21.stream.Measure 140 offset=422.0>
<music21.note.Note G#>
<music21.note.Note A>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note G>
<music21.note.Note B>
<music21.stream.Measure 141 offset=425.0>
<music21.note.Note G#>
<music21.note.Note A>
<music21.note.Note F#>
<music21.note.Note G#>
<music21.note.Note A>
<music21.note.Note F#>
<music21.stream.Measure 142 offset=428.0>
<music21.tempo.MetronomeMark Quarter=97.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 143 offset=431.0>
<music21.tempo.MetronomeMark moderate Quarter=94.0>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Note F#>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Note F#>
<music21.stream.Measure 144 offset=434.0>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Rest dotted-half>
<music21.stream.Measure 145 offset=437.0>
<music21.tempo.MetronomeMark maestoso Quarter=86.0>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark andantino Quarter=80.0>
<music21.note.Rest quarter>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Measure 146 offset=440.0>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note C>
<music21.note.Note C>
<music21.note.Note C>
<music21.stream.Measure 147 offset=443.0>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Measure 148 offset=446.0>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.stream.Measure 149 offset=449.0>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.note.Note G>
<music21.note.Note G>
<music21.note.Note G>
<music21.stream.Measure 150 offset=452.0>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note C>
<music21.note.Note C>
<music21.note.Note C>
<music21.stream.Measure 151 offset=455.0>
<music21.note.Note B>
<music21.note.Rest eighth>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.stream.Measure 152 offset=458.0>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note C>
<music21.note.Note D>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Note B>
<music21.note.Note D>
<music21.stream.Measure 153 offset=461.0>
<music21.stream.Voice 0x103268a00>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Voice 0x103268b20>
<music21.note.Note C>
<music21.note.Note B>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.stream.Measure 154 offset=464.0>
<music21.note.Note C>
<music21.note.Rest eighth>
<music21.chord.Chord C4 A3>
<music21.stream.Measure 155 offset=467.0>
<music21.chord.Chord D4 B3>
<music21.note.Rest eighth>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note D>
<music21.stream.Measure 156 offset=470.0>
<music21.note.Note C>
<music21.note.Rest eighth>
<music21.note.Note A>
<music21.note.Note C>
<music21.note.Note A>
<music21.note.Note C>
<music21.note.Note A>
<music21.note.Note C>
<music21.stream.Measure 157 offset=473.0>
<music21.note.Note B>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note G>
<music21.stream.Measure 158 offset=476.0>
<music21.note.Note D>
<music21.note.Note G>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note G>
<music21.note.Note D>
<music21.stream.Measure 159 offset=479.0>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note G>
<music21.note.Note D>
<music21.note.Note B>
<music21.stream.Measure 160 offset=482.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.note.Rest eighth>
<music21.stream.Measure 161 offset=485.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark Quarter=100.0>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note G>
<music21.stream.Measure 162 offset=488.0>
<music21.stream.Voice 0x10326a9e0>
<music21.note.Note D>
<music21.note.Note G>
<music21.note.Note B>
<music21.note.Note G>
<music21.note.Note D>
<music21.stream.Voice 0x10326ace0>
<music21.note.Rest 1.25ql>
<music21.note.Note D>
<music21.note.Rest 1.25ql>
<music21.stream.Measure 163 offset=491.0>
<music21.stream.Voice 0x10326ae90>
<music21.note.Note B>
<music21.note.Note D>
<music21.note.Note G>
<music21.note.Note D>
<music21.note.Note B>
<music21.stream.Voice 0x10326b190>
<music21.note.Rest 1.25ql>
<music21.note.Note B>
<music21.note.Rest 1.25ql>
<music21.stream.Measure 164 offset=494.0>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Note C>
<music21.note.Note D>
<music21.note.Note E>
<music21.note.Note F#>
<music21.note.Note G>
<music21.note.Note A>
<music21.note.Note D>
<music21.note.Note E>
<music21.note.Note F#>
<music21.stream.Measure 165 offset=497.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.note.Note D>
<music21.note.Rest eighth>
<music21.stream.Measure 166 offset=500.0>
<music21.note.Note G>
<music21.note.Rest eighth>
<music21.tempo.MetronomeMark Quarter=96.0>
<music21.chord.Chord D2 D3>
<music21.tempo.MetronomeMark maestoso Quarter=90.0>
<music21.tempo.MetronomeMark andantino Quarter=80.0>
<music21.note.Rest eighth>
<music21.stream.Measure 167 offset=503.0>
<music21.chord.Chord G2 G3>
<music21.note.Rest dotted-quarter>
<music21.bar.Barline type=final>
"""