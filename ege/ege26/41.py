with open('26data/26-j10.txt') as input_file:
    d_disk, e_disk, useless = [int(i) for i in input_file.readline().split()]
    e_files = []
    d_files = []
    for i in input_file:
        if int(i) > 500:
            d_files.append(int(i))
        else:
            e_files.append(int(i))
    d_files.sort()
    e_files.sort()
e_almost_max = 0
d_almost_max = 0
counter = 0
for i in range(len(e_files)):
    if e_disk - e_files[i] < 0:
        break
    else:
        counter += 1
        e_disk -= e_files[i]
        e_almost_max = e_files[i]

for i in range(len(d_files)):
    if d_disk - d_files[i] < 0:
        break
    else:
        counter += 1
        d_disk -= d_files[i]
        d_almost_max = d_files[i]
print(counter)

for i in range(e_disk + e_almost_max + 1, 10, -1):
    try:
        print(i, e_files.index(i))
        break
    except:
        pass
for i in range(d_disk + d_almost_max + 1, 10, -1):
    try:
        print(i, d_files.index(i))
        break
    except:
        pass
