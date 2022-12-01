list = [[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]], 
        [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]]]
list_b = []
list_c = []
count = 3 

for channel in list:
    mem4 = []
    mem4 = channel[:3]
    list_b.append(mem4)
print(list_b)

for channel in list_b:
    mem5 = []
    count += 1
    mem5 = channel[4]
    list_c.append(mem5)
print(list_c)

for channel in list_b:
    channel.pop(0)
    channel.append()

print(list_b)