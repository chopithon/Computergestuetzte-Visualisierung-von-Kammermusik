from music21 import *
sBach = converter.parse('vns_rnd.mid')
parts = []
notes = []

for p in sBach.parts:
    parts.append(p.id)

for part in parts:
    for n in part.pitches:
        notes.append(n)

