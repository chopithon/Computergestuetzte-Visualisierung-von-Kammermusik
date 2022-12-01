from tkinter import W
from mido import MidiFile

mid = MidiFile('vns_rnd.mid')
count_tracks = 0

for i, track in enumerate(mid.tracks):
    print(i, track.name)
    count_tracks += 1

def get_pitch_list(count_tracks):
    if count_tracks == 1:
        pitch_0 = []
        print("only one track!")
        return pitch_0

    elif count_tracks == 2:
        pitch_0 = []
        pitch_1 = []
        return pitch_0, pitch_1

    elif count_tracks == 3:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        return pitch_0, pitch_1, pitch_2

     

    elif count_tracks == 7:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6

    elif count_tracks == 8:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7

    elif count_tracks == 9:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        pitch_8 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7, pitch_8

    elif count_tracks == 10:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        pitch_8 = []
        pitch_9 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7, pitch_8, pitch_9

    elif count_tracks == 11:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        pitch_8 = []
        pitch_9 = []
        pitch_10 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7, pitch_8, pitch_9, pitch_10

    elif count_tracks == 12:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        pitch_8 = []
        pitch_9 = []
        pitch_10 = []
        pitch_11 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7, pitch_8, pitch_9, pitch_10, pitch_11

    elif count_tracks == 13:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        pitch_8 = []
        pitch_9 = []
        pitch_10 = []
        pitch_11 = []
        pitch_12 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7, pitch_8, pitch_9, pitch_10, pitch_11, pitch_12

    elif count_tracks == 14:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        pitch_8 = []
        pitch_9 = []
        pitch_10 = []
        pitch_11 = []
        pitch_12 = []
        pitch_13 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7, pitch_8, pitch_9, pitch_10, pitch_11, pitch_12, pitch_13


    elif count_tracks == 15:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        pitch_8 = []
        pitch_9 = []
        pitch_10 = []
        pitch_11 = []
        pitch_12 = []
        pitch_13 = []
        pitch_14 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7, pitch_8, pitch_9, pitch_10, pitch_11, pitch_12, pitch_13, pitch_14

    elif count_tracks == 16:
        pitch_0 = []
        pitch_1 = []
        pitch_2 = []
        pitch_3 = []
        pitch_4 = []
        pitch_5 = []
        pitch_6 = []
        pitch_7 = []
        pitch_8 = []
        pitch_9 = []
        pitch_10 = []
        pitch_11 = []
        pitch_12 = []
        pitch_13 = []
        pitch_14 = []
        pitch_15 = []
        return pitch_0, pitch_1, pitch_2, pitch_3, pitch_4, pitch_5, pitch_6, pitch_7, pitch_8, pitch_9, pitch_10, pitch_11, pitch_12, pitch_13, pitch_14, pitch_15
