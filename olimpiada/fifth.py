def calculate(listic):
    x = sorted(listic, reverse=True)
    q = max(x)
    u = []
    for j in range(q):
        u.append(1)
        r = 1
        for index in range(len(x)):
            if index + r < len(x):
                if x[index] - x[index + r] == j:
                    u[-1] += 1
                    r = 1
                elif x[index] - x[index + r] < j:
                    for k in range(r):
                        if x[index] - x[index + k] == j:
                            u[-1] += 1
                else:
                    r += 1
            elif u[-1] < len(x) and min(x) - j < 0:
                u[-1] += 1
        if max(u) == len(x):
            return max(u)
    return max(u)


for i in range(int(input())):
    input()
    print(f'Case #{i + 1}:', calculate([int(i) for i in input().split()]))
