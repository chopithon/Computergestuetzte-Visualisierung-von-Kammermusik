# https://stackoverflow.com/questions/22612119/showing-midi-pitch-numbers-from-mid-file-with-music21

from music21 import *

file = converter.parse('bth-trio.mid')

instruments = file.getInstruments()
instruments.show("text")