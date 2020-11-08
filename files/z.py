i = open("input.txt")
o = open("output.txt", "w")
min = 0
max = 0
f = 1
for j in i:
    j = int(j)
    if j % 2 == 0 and j > 0:
        if f:
            min = j
            f = 0
        if j > max:
            max = j
        if j < min:
            min = j
if max != 0:
    print(min, max, file=o)
else:
    print("0", file=o)
i.close()
o.close()