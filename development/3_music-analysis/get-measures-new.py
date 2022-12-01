from music21 import *
from re import fullmatch

file = converter.parse('vns_rnd.mid')

components = []
str_components = []
analyse_chords = []
chords = []

pattern_measure = r"<(music21\.stream\.Measure)\s+[0-9]?[0-9]?[0-9]+\s(offset)\=[0-9]?[0-9]?[0-9]\.[0-9]>"
count_measure = 0

def get_chords(input):
    sChords = input.chordify()
    sFlat = sChords.flatten()
    sOnlyChords = sFlat.getElementsByClass('Chord')
    displayPart = stream.Part(id='displayPart')

    for i in range(0, len(sOnlyChords) - 1):
        thisChord = sOnlyChords[i]
        nextChord = sOnlyChords[i + 1]

    def appendChordPairs(thisChord, nextChord):
        if ((thisChord.isTriad() is True or
                thisChord.isSeventh() is True) and
                    thisChord.root().name == 'A'):
            closePositionThisChord = thisChord.closedPosition(forceOctave=4)
            closePositionNextChord = nextChord.closedPosition(forceOctave=4)

            m = stream.Measure()
            m.append(closePositionThisChord)
            m.append(closePositionNextChord)
            displayPart.append(m)

    allChords = []

    for i in range(len(sOnlyChords) - 1):
        thisChord = sOnlyChords[i]
        basedChord = thisChord.bass()
        namedChord = basedChord.name
        strChord = str(namedChord)

        #print(strChord)
        """
        if strChord == "E-":
            print("yes")
        """

        allChords.append(strChord)

        nextChord = sOnlyChords[i + 1]
        appendChordPairs(thisChord, nextChord)

    return allChords

for element in file.recurse():
    components.append(element)
    str_components.append(str(element))

for str_element in str_components:
    m = fullmatch(pattern_measure, str_element)

    if m:
        count_measure += 1

        chords.append(count_measure)
        chords.append(get_chords(analyse_chords))



    else: 
        analyse_chords.append(str_element)

print(chords)