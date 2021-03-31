pole = [[0] * 100 for i in range(100)]
pole[49][49] = 1

x = 49
y = 49
pov = 0
shag = 0
string = input()
for i in string:
    if i == 'L':
        if pov == 0:
            pov = 3
        else:
            pov -= 1
    elif i == 'R':
        if pov == 3:
            pov = 0
        else:
            pov += 1
    if i == 'S':
        if pov == 0:
            x -= 1
        elif pov == 1:
            y += 1
        elif pov == 2:
            x += 1
        elif pov == 3:
            y -= 1
        if pole[x][y] == 1:
            print(shag + 1)
            exit(0)
        else:
            pole[x][y] = 1
        shag += 1
print(-1)