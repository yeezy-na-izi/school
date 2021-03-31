line = input()
step = direction = x = y = 0
lst = ['0 0']
for i in line:
    if i == 'R':
        direction = (direction + 1) % 4
    elif i == 'L':
        direction = (direction + 3) % 4
    else:
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        else:
            x -= 1
        step += 1
    if i == 'S':
        if (str(x) + ' ' + str(y)) in lst:
            print(step)
            exit(0)
        lst.append(str(x) + ' ' + str(y))
print(-1)
