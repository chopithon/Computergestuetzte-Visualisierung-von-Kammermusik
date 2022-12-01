from music21 import *

file = converter.parse('vns_rnd.mid')

analysis_file = analysis.reduction.PartReduction(fillByMeasure = True)

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

for i in analysis_file: 
    get_chords(i)