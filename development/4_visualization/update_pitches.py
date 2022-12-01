count_pitch_i = 0
all_pitches_d_m = []
all_pitches_d_m_a = []
instruments = 3
count = 0
while count < instruments:
    listed = []
    all_pitches_d_m.append(listed)
    count += 1

count = 0
counter = 300
count_1 = 0
count_True = 0
for listed in all_pitches_d_m:
    while count < counter:
        listed.append(count)
        count += 1
        if count_1 == 0:
            count_True += 1
            if count_True >= 20:
                listed.append("True")
    count = 0
    count_1 = 1
    all_pitches_d_m_a.append(listed)

# aim: def() get new pitches, each instr-list contains 100 element, 
# first instruments list doesn't contain any "True"-element but has len = 100

count_thickness_i = 101 # count index of thickness and other pitches 
count_pitches_i = 152 # count index of first instr pitch
count_1 = 0 # count instr No. I
count_100 = 0 # count 100 elements
pitches_100 = []

for instr in all_pitches_d_m_a:
    pitch_100 = []
    count_pitches_100 = count_thickness_i
    all_pitches = instr
    if count_1 == 0:
        count_pitches_100 = count_pitches_i
        while count_100 < 100:
            count_100 += 1
            count_pitches_100 += 1
            new_pitch = all_pitches[count_pitches_100]
            if new_pitch == "True":
                color = "red"
                count_100 -= 1
            else:
                pitch_100.append(new_pitch)        
        count_1 = 1
    else:
        while count_100 < 100:
            count_100 += 1
            count_pitches_100 += 1
            pitch_100.append(all_pitches[count_pitches_100])
    count_100 = 0
    pitches_100.append(pitch_100)

print(pitches_100)

"""
for instr in all_pitches_d_m_a:
    if count_0 == 0:
        while count < count_pitch_i:
            instr.pop(0)
            #print(len(pitch_d_m_a))
            count += 1
            #print(count)

        count_0 = 1
        all_pitches_d_m_a.append(instr) 

    else:
        while count < count_thickness_i:
            instr.pop(0)
            count += 1

        all_pitches_d_m_a.append(instr)

    count = 0
"""