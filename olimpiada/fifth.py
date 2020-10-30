qwe = [int(input()) for _ in range(int(input()))]

for i in range(len(qwe)):
    anoth = qwe[:i] + qwe[i + 1:]
    cell = qwe[i]
    for x in anoth:
        if cell > x:
            cell += x
        else:
            print(0)
            break
    else:
        print(1)