a = open('input.txt', 'r')
b = open('output.txt', 'w')
z = []
x = 0
for i in a:
    i = i.split()
    if len(i) == 1:
        x = int(i[0])
    elif int(i[1]) < x:
        z.append(i)
for i in z:
    b.write(' '.join(i) + '\n')
b.write(str(len(z)))
