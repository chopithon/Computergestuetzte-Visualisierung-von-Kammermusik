from music21 import converter,instrument # or import *
from re import fullmatch

pattern_measure = r"<(music21\.stream\.Measure)\s+[0-9]?[0-9]?[0-9]+\s(offset)\=[0-9]?[0-9]?[0-9]\.[0-9]>"
string_1 = "<music21.note.Note F#>"
string_2 = "<music21.stream.Measure 135 offset=407.0>"

m = fullmatch(pattern_measure, string_1)
print(m)