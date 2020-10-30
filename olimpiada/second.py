a = int(input())
b = int(input())
if (a + b) % 3 == 0:
    s = (a + b) // 3
    f = True
    if s <= a and s <= b:
        if a < b:
            f = False
        d = (s + abs(a - b)) // 2
        if f:
            print(f'{d} {s - d}')
        else:
            print(f'{s - d} {d}')
    else:
        print(-1)
else:
    print(-1)
