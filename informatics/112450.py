m, n = [int(i) for i in input().split()]
n *= 2
n += 1
s = [x for x in range(2, n + 1) if
     x not in [i for sub in [list(range(2 * j, n + 1, j)) for j in range(2, n // 2)] for i in sub]]
string = ''
for i in range(m, (n - 1) // 2):
    if i in s and i * 2 + 1 in s:
        string += f'{i} '
print(string.rstrip() if string else 0)

