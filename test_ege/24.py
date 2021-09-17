q = []
maxim = 0
bo = False
for i in range(int(input())):
    x = int(input())
    if x > 100:
        if bo:
            bo = False
            q.append(x - x / 10)
            if x > maxim:
                maxim = x
        else:
            q.append(x)
            bo = True
    else:
        q.append(x)
print(maxim, sum(q))