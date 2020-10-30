per = int(input())
L = int(input())
z = L // per
if L - z * per > (z + 1) * per - L:
    vivod = (z + 1) * per - L
else:
    vivod = L - z * per
print(vivod)
