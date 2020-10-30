n = int(input())
z = int(((n - 1) ** 0.5) + 1)
vivod = [0, 0]
if z % 2 == 0:
    if n >= z ** 2 - z:
        vivod[1] = z ** 2 - n + 1
        vivod[0] = z
    else:
        vivod[1] = z
        vivod[0] = n - (z - 1) ** 2
else:
    if n >= z ** 2 - z:
        vivod[0] = z ** 2 - n + 1
        vivod[1] = z
    else:
        vivod[0] = z
        vivod[1] = n - (z - 1) ** 2
print(*vivod)