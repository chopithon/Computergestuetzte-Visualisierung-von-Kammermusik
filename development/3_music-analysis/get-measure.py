from itertools import count
from music21 import converter,instrument # or import *
from re import fullmatch

file = converter.parse('vns_rnd.mid')
components = []
str_components = []
measures = []
analyse_chords = []
chords = []
pattern_measure = r"<(music21\.stream\.Measure)\s+[0-9]?[0-9]?[0-9]+\s(offset)\=[0-9]?[0-9]?[0-9]\.[0-9]>"
count_elements = 0
count_measure = 1
count_components_id = 0

for element in file.recurse():
    components.append(element)
    str_components.append(str(element))

for str_element in str_components:
    m = fullmatch(pattern_measure, str_element)

    if m:
        measures.append(count_elements)
        while count_elements < count_components_id:
            analyse_chords.append(components[count_elements])
            count_elements += 1

        count_measure += 1
        count_elements = 0

    else:
        count_elements += 1
    
    count_components_id += 1

#print(components)
print(measures)
print(analyse_chords)
