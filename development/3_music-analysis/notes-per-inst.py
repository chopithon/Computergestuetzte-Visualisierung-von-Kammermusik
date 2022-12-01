# https://splunktool.com/music21-get-all-notes-per-instrument-from-a-midi-file

from music21 import *

file = corpus.parse('bwv66.6')

components = []

for element in file.recurse():
   components.append(str(element))

for i in components:
   print(i)

# output
"""
<music21.metadata.Metadata object at 0x102fa7a90>
<music21.stream.Part Soprano>
P1: Soprano: Instrument 1
<music21.stream.Measure 0 offset=0.0>
<music21.clef.TrebleClef>
f# minor
<music21.meter.TimeSignature 4/4>
<music21.note.Note C#>
<music21.note.Note B>
<music21.stream.Measure 1 offset=1.0>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Note C#>
<music21.note.Note E>
<music21.stream.Measure 2 offset=5.0>
<music21.note.Note C#>
<music21.note.Note B>
<music21.note.Note A>
<music21.note.Note C#>
<music21.stream.Measure 3 offset=9.0>
<music21.layout.SystemLayout>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Note G#>
<music21.note.Note F#>
<music21.note.Note A>
<music21.stream.Measure 4 offset=13.0>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note F#>
<music21.note.Note E>
<music21.stream.Measure 5 offset=17.0>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Note C#>
<music21.note.Note C#>
<music21.stream.Measure 6 offset=21.0>
<music21.layout.SystemLayout>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Note C#>
<music21.note.Note A>
<music21.stream.Measure 7 offset=25.0>
<music21.note.Note G#>
<music21.note.Note F#>
<music21.note.Note G#>
<music21.stream.Measure 8 offset=29.0>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.stream.Measure 9 offset=33.0>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note E#>
<music21.note.Note F#>
<music21.bar.Barline type=final>
<music21.stream.Part Alto>
P2: Alto: Instrument 2
<music21.stream.Measure 0 offset=0.0>
<music21.clef.TrebleClef>
f# minor
<music21.meter.TimeSignature 4/4>
<music21.note.Note E>
<music21.stream.Measure 1 offset=1.0>
<music21.note.Note F#>
<music21.note.Note E>
<music21.note.Note E>
<music21.note.Note E>
<music21.stream.Measure 2 offset=5.0>
<music21.note.Note E>
<music21.note.Note A>
<music21.note.Note G#>
<music21.note.Note E>
<music21.note.Note G#>
<music21.stream.Measure 3 offset=9.0>
<music21.layout.SystemLayout>
<music21.note.Note F#>
<music21.note.Note G#>
<music21.note.Note E#>
<music21.note.Note C#>
<music21.note.Note F#>
<music21.stream.Measure 4 offset=13.0>
<music21.note.Note F#>
<music21.note.Note E>
<music21.note.Note D#>
<music21.note.Note C#>
<music21.stream.Measure 5 offset=17.0>
<music21.note.Note C#>
<music21.note.Note F#>
<music21.note.Note E>
<music21.note.Note E>
<music21.note.Note A>
<music21.stream.Measure 6 offset=21.0>
<music21.layout.SystemLayout>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note G#>
<music21.note.Note F#>
<music21.stream.Measure 7 offset=25.0>
<music21.note.Note F#>
<music21.note.Note E#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.note.Note C#>
<music21.stream.Measure 8 offset=29.0>
<music21.note.Note C#>
<music21.note.Note D>
<music21.note.Note E>
<music21.note.Note D>
<music21.note.Note C#>
<music21.stream.Measure 9 offset=33.0>
<music21.note.Note B>
<music21.note.Note C#>
<music21.note.Note D>
<music21.note.Note C#>
<music21.bar.Barline type=final>
<music21.stream.Part Tenor>
P3: Tenor: Instrument 3
<music21.stream.Measure 0 offset=0.0>
<music21.clef.BassClef>
f# minor
<music21.meter.TimeSignature 4/4>
<music21.note.Note A>
<music21.note.Note B>
<music21.stream.Measure 1 offset=1.0>
<music21.note.Note C#>
<music21.note.Note B>
<music21.note.Note A>
<music21.note.Note B>
<music21.stream.Measure 2 offset=5.0>
<music21.note.Note A>
<music21.note.Note E>
<music21.note.Note E>
<music21.note.Note D>
<music21.note.Note C#>
<music21.note.Note C#>
<music21.stream.Measure 3 offset=9.0>
<music21.layout.SystemLayout>
<music21.note.Note C#>
<music21.note.Note D>
<music21.note.Note C#>
<music21.note.Note B>
<music21.note.Note A>
<music21.note.Note C#>
<music21.stream.Measure 4 offset=13.0>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note A>
<music21.note.Note G#>
<music21.stream.Measure 5 offset=17.0>
<music21.note.Note F#>
<music21.note.Note D>
<music21.note.Note C#>
<music21.note.Note B>
<music21.note.Note A>
<music21.note.Note E>
<music21.stream.Measure 6 offset=21.0>
<music21.layout.SystemLayout>
<music21.note.Note D>
<music21.note.Note D>
<music21.note.Note C#>
<music21.note.Note C#>
<music21.stream.Measure 7 offset=25.0>
<music21.note.Note D>
<music21.note.Note C#>
<music21.note.Note C#>
<music21.note.Note B>
<music21.note.Note E#>
<music21.stream.Measure 8 offset=29.0>
<music21.note.Note F#>
<music21.note.Note C#>
<music21.note.Note B>
<music21.note.Note A#>
<music21.stream.Measure 9 offset=33.0>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note A#>
<music21.bar.Barline type=final>
<music21.stream.Part Bass>
P4: Bass: Instrument 4
<music21.stream.Measure 0 offset=0.0>
<music21.clef.BassClef>
f# minor
<music21.meter.TimeSignature 4/4>
<music21.note.Note A>
<music21.note.Note G#>
<music21.stream.Measure 1 offset=1.0>
<music21.note.Note F#>
<music21.note.Note G#>
<music21.note.Note A>
<music21.note.Note G#>
<music21.stream.Measure 2 offset=5.0>
<music21.note.Note A>
<music21.note.Note C#>
<music21.note.Note E>
<music21.note.Note A>
<music21.note.Note E#>
<music21.stream.Measure 3 offset=9.0>
<music21.layout.SystemLayout>
<music21.note.Note F#>
<music21.note.Note B>
<music21.note.Note C#>
<music21.note.Note F#>
<music21.note.Note F#>
<music21.stream.Measure 4 offset=13.0>
<music21.note.Note G#>
<music21.note.Note F#>
<music21.note.Note G#>
<music21.note.Note A>
<music21.note.Note B>
<music21.note.Note B>
<music21.note.Note C#>
<music21.stream.Measure 5 offset=17.0>
<music21.note.Note F#>
<music21.note.Note G#>
<music21.note.Note A>
<music21.note.Note A>
<music21.stream.Measure 6 offset=21.0>
<music21.layout.SystemLayout>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note E#>
<music21.note.Note F#>
<music21.stream.Measure 7 offset=25.0>
<music21.note.Note B>
<music21.note.Note C#>
<music21.note.Note D>
<music21.note.Note C#>
<music21.stream.Measure 8 offset=29.0>
<music21.note.Note A#>
<music21.note.Note B>
<music21.note.Note C#>
<music21.stream.Measure 9 offset=33.0>
<music21.note.Note D>
<music21.note.Note B>
<music21.note.Note F#>
<music21.bar.Barline type=final>
<music21.layout.StaffGroup <music21.stream.Part Soprano><music21.stream.Part Alto><music21.stream.Part Tenor><music21.stream.Part Bass>>
"""