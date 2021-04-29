n, sec = [int(i) for i in input().split()]
a = [[0 for i in range(n + 2)]]
for i in range(n):
    a.append([0] + [int(i) for i in input().split()] + [0])
a.append([0 for i in range(n + 2)])
for _ in range(sec):
    for i in range(n):
        for j in range(n):
            pass