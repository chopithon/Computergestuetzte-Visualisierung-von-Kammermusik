z_all = [50, 50, 57, 57, 66, 66, 64, 64, 66, 50, 66, 50, 57, 57, 66, 45, 66, 45, 57, 57, 38, 38, 57, 57, 66, 66, 64, 64, 66, 50, 66, 50, 57, 57, 66, 47, 66, 47, 57, 57, 38, 38, 59, 59, 67, 67, 66, 66, 67, 52, 67, 52, 59, 59, 50, 50, 59, 59, 38, 38, 59, 59, 67, 49, 67, 49, 66, 66, 67, 67, 59, 59, 67, 50, 67, 50, 59, 59, 50, 50, 61, 61, 67, 67, 66, 66, 67, 52, 67, 52, 61, 61, 67, 50, 67, 50, 61, 61, 38, 38, 61, 61, 67, 67, 66, 66, 67, 45, 67, 45, 61, 61, 67, 52, 67, 52, 61, 61, 38, 38, 62, 62, 66, 66, 64, 64, 66, 45, 66, 45, 62, 62, 66, 66, 62, 62, 47, 47, 62, 62, 66, 66, 64, 64, 66, 49, 66, 49, 62, 62, 66, 66, 61, 61, 38, 38, 59, 59, 66, 66, 64, 64, 66, 50, 66, 50, 62, 62, 61, 61, 62, 62, 59, 52, 59, 52, 62, 62, 61, 61, 62, 62, 54, 54, 57, 57, 56, 56, 54, 54, 56, 56, 62, 62, 64, 54, 64, 54, 62, 62, 64, 52, 64, 52, 62, 62, 64, 50, 64, 50, 62, 62, 56, 49, 56, 49, 62, 62, 64, 47, 64, 47, 62, 62, 64, 45, 64, 45, 62, 62, 64, 44, 64, 44, 62, 62, 61, 57, 45, 61, 57, 45, 64, 64, 69, 69, 68, 68, 69, 69, 64, 64, 62, 62, 64, 64, 61, 45, 61, 45, 64, 64, 62, 62, 64, 64, 57, 57, 61, 61, 59, 59, 57, 57, 47, 47, 54, 54, 62, 62, 61, 61, 62, 62, 54, 54, 62, 62, 54, 54, 45, 45, 54, 54, 62, 62, 61, 61, 62, 47, 62, 47, 54, 54, 62, 45, 62, 45, 54, 54, 44, 44, 59, 59, 57, 57, 59, 59, 57, 57, 56, 56, 54, 54, 52, 52, 62, 40, 62, 40, 61, 61, 59, 59, 69, 69, 68, 68, 66, 66, 64, 64, 62, 62, 61, 45, 61, 45, 59, 59, 57, 57, 69, 69, 64, 64, 69, 69, 61, 61, 64, 64, 57, 45, 57, 45, 59, 59, 61, 61, 64, 64, 62, 62, 61, 61, 59, 59, 57, 57, 63, 47, 63, 47, 57, 57, 59, 59, 60, 60, 59, 59, 57, 57, 63, 63, 57, 57, 66, 47, 66, 47, 57, 57, 59, 59, 60, 60, 59, 59, 57, 57, 63, 63, 57, 57, 55, 40, 55, 40, 59, 59, 64, 64, 66, 66, 67, 67, 64, 64, 59, 59, 57, 57, 55, 55, 59, 59, 64, 64, 66, 66, 67, 67, 64, 64, 61, 61, 59, 59, 63, 45, 63, 45, 57, 57, 60, 60, 59, 59, 60, 60, 57, 57, 63, 54, 63, 54, 57, 57, 66, 47, 66, 47, 57, 57, 60, 60, 59, 59, 60, 60, 57, 57, 63, 54, 63, 54, 57, 57, 55, 43, 55, 43, 59, 59, 64, 64, 66, 66, 67, 67, 64, 64, 59, 59, 57, 57, 55, 40, 55, 40, 59, 59, 64, 54, 64, 54, 66, 66, 67, 52, 67, 52, 64, 64, 61, 61, 59, 59, 58, 42, 58, 42, 61, 61, 58, 58, 61, 61, 64, 55, 64, 55, 59, 59, 64, 54, 64, 54, 61, 61, 58, 52, 58, 52, 61, 61, 58, 58, 61, 61, 64, 50, 64, 50, 61, 61, 64, 49, 64, 49, 61, 61, 62, 47, 62, 47, 61, 61, 59, 59, 62, 62, 61, 55, 61, 55, 62, 62, 64, 52, 64, 52, 61, 61, 62, 47, 62, 47, 61, 61, 59, 59, 57, 57, 55, 55, 54, 54, 52, 52, 50, 50, 49, 49, 55, 55, 57, 57, 55, 55, 57, 57, 55, 55, 57, 57, 55, 55, 49, 40, 49, 40, 55, 55, 57, 57, 55, 55, 57, 57, 55, 55, 57, 57, 55, 55, 50, 50, 54, 54, 60, 60, 59, 59, 60, 38, 60, 38, 54, 54, 60, 60, 54, 54, 50, 50, 54, 54, 60, 60, 59, 59, 60, 60, 54, 54, 60, 60, 54, 54, 50, 50, 55, 55, 59, 59, 57, 57, 59, 38, 59, 38, 55, 55, 59, 59, 55, 55, 50, 50, 55, 55, 59, 59, 57, 57, 59, 38, 59, 38, 55, 55, 59, 59, 55, 55, 50, 50, 61, 61, 67, 67, 66, 66, 67, 67, 61, 61, 67, 67, 61, 61, 50, 50, 61, 61, 67, 38, 67, 38, 66, 66, 67, 67, 61, 61, 67, 67, 61, 61, 50, 50, 62, 62, 66, 66, 64, 64, 66, 38, 66, 38, 62, 62, 61, 61, 59, 59, 57, 57, 55, 55, 54, 54, 52, 52, 50, 50, 49, 49, 47, 47, 45, 45, 44, 44, 52, 52, 59, 59, 61, 61, 62, 62, 59, 59, 61, 61, 62, 62, 44, 44, 52, 52, 59, 59, 61, 61, 62, 62, 59, 59, 61, 61, 62, 62, 43, 43, 52, 52, 57, 57, 59, 59, 61, 61, 57, 57, 59, 59, 61, 61, 43, 43, 52, 52, 57, 57, 59, 59, 61, 61, 57, 57, 59, 59, 61, 61, 43, 43, 52, 52, 57, 57, 61, 61, 66, 66, 68, 68, 69, 61, 57, 52, 45, 69, 61, 57, 52, 45, 52, 52, 54, 54, 55, 55, 57, 57, 59, 59, 61, 61, 62, 62, 64, 45, 64, 45, 61, 61, 57, 57, 59, 59, 61, 54, 61, 54, 62, 62, 64, 52, 64, 52, 66, 66, 67, 50, 67, 50, 64, 64, 61, 49, 61, 49, 62, 62, 64, 47, 64, 47, 66, 66, 67, 45, 67, 45, 69, 69, 70, 61, 57, 45, 70, 61, 57, 45, 69, 69, 68, 68, 69, 69, 69, 62, 58, 69, 62, 58, 67, 67, 66, 66, 69, 69, 67, 61, 57, 67, 61, 57, 64, 64, 61, 61, 59, 59, 57, 57, 55, 55, 54, 54, 55, 55, 45, 45, 52, 52, 57, 57, 61, 61, 64, 64, 66, 66, 67, 67, 64, 64, 66, 45, 66, 45, 62, 62, 57, 57, 55, 55, 54, 54, 50, 50, 52, 52, 54, 54, 45, 45, 50, 50, 54, 54, 57, 57, 62, 62, 64, 64, 66, 66, 62, 62, 68, 62, 57, 45, 68, 62, 57, 45, 65, 65, 64, 64, 65, 65, 65, 59, 56, 47, 65, 59, 56, 47, 64, 64, 63, 63, 64, 64, 64, 64, 62, 62, 61, 61, 62, 62, 59, 59, 57, 57, 56, 56, 54, 54, 52, 52, 56, 56, 59, 59, 62, 62, 64, 50, 64, 50, 68, 68, 69, 69, 68, 68, 69, 45, 69, 45, 64, 64, 61, 61, 59, 59, 61, 42, 61, 42, 64, 64, 57, 57, 61, 61, 52, 52, 57, 57, 56, 56, 54, 54, 52, 45, 52, 45, 50, 50, 49, 49, 47, 47, 45, 45, 67, 47, 67, 47, 66, 66, 64, 49, 64, 49, 62, 62, 61, 50, 61, 50, 59, 59, 57, 52, 57, 52, 67, 67, 66, 59, 66, 59, 64, 64, 62, 55, 62, 55, 61, 61, 59, 50, 59, 50, 57, 57, 55, 47, 55, 47, 66, 66, 64, 64, 62, 62, 61, 61, 59, 59, 57, 57, 55, 55, 54, 45, 54, 45, 64, 64, 62, 47, 62, 47, 61, 61, 59, 50, 59, 50, 57, 57, 55, 38, 55, 38, 54, 54, 52, 43, 52, 43, 62, 62, 61, 61, 59, 59, 61, 45, 61, 45, 64, 64, 57, 49, 57, 49, 64, 64, 59, 50, 59, 50, 64, 64, 61, 52, 61, 52, 64, 64, 62, 54, 62, 54, 64, 64, 59, 56, 59, 56, 64, 64, 61, 52, 45, 61, 52, 45, 64, 64, 57, 49, 57, 49, 64, 64, 62, 54, 62, 54, 64, 64, 59, 50, 59, 50, 64, 64, 61, 52, 61, 52, 64, 64, 57, 49, 57, 49, 64, 64, 62, 54, 62, 54, 64, 64, 59, 50, 59, 50, 64, 64, 61, 45, 61, 45, 64, 64, 57, 57, 64, 64, 59, 59, 64, 64, 61, 61, 64, 64, 62, 62, 64, 64, 64, 64, 64, 64, 66, 66, 64, 64, 45, 45, 64, 64, 64, 64, 64, 64, 66, 66, 64, 64, 67, 67, 64, 64, 45, 45, 64, 64, 66, 66, 64, 64, 67, 67, 64, 64, 69, 69, 64, 64, 66, 66, 64, 64, 67, 67, 64, 64, 66, 66, 64, 64, 67, 67, 64, 64, 64, 64, 64, 64, 66, 66, 64, 64, 64, 64, 64, 64, 66, 66, 64, 64, 62, 62, 64, 64, 64, 64, 64, 64, 62, 62, 64, 64, 64, 64, 64, 64, 61, 61, 64, 64, 62, 62, 64, 64, 61, 61, 64, 64, 62, 62, 64, 64, 59, 59, 64, 64, 61, 61, 64, 64, 57, 57, 59, 59, 60, 57, 60, 57, 45, 45, 61, 58, 61, 58, 45, 45, 62, 59, 62, 59, 45, 45, 63, 60, 63, 60, 45, 45, 64, 55, 64, 55, 45, 45, 65, 56, 65, 56, 45, 45, 66, 57, 66, 57, 45, 45, 67, 58, 67, 58, 45, 45, 68, 59, 68, 59, 45, 45, 69, 60, 69, 60, 45, 45, 70, 61, 70, 61, 45, 45, 71, 62, 71, 62, 45, 45, 72, 63, 72, 63, 45, 45, 73, 64, 73, 64, 45, 45, 74, 45, 74, 45, 66, 66, 62, 62, 66, 66, 74, 74, 66, 66, 74, 74, 66, 66, 74, 45, 74, 45, 66, 66, 62, 62, 66, 66, 74, 74, 66, 66, 74, 74, 66, 66, 74, 45, 74, 45, 64, 64, 57, 57, 64, 64, 74, 74, 64, 64, 74, 74, 64, 64, 74, 45, 74, 45, 64, 64, 57, 57, 64, 64, 74, 74, 64, 64, 74, 74, 64, 64, 73, 45, 73, 45, 64, 64, 57, 57, 64, 64, 73, 67, 73, 67, 64, 64, 73, 67, 73, 67, 64, 64, 73, 67, 45, 73, 67, 45, 64, 64, 57, 57, 64, 64, 73, 67, 73, 67, 64, 64, 73, 67, 45, 73, 67, 45, 64, 64, 38, 45, 50, 62, 66, 74, 74, 66, 62, 50, 45, 38]
z = z_all[:100]

count = 100
def schritt():
    global count, z
    
    if count < len(z_all):
        z.pop(0)
        z.append(z_all[count])
        count += 1
    
    else:
        z = z

    print(z)
    print(count)

while count < len(z_all):
    schritt()
