useless, n = [int(i) for i in input().split()]
coins = [0] + [int(i) for i in input().split()] + [0] * n
money = [[0, []] for i in range(useless + n + 1)]
for i in range(useless - 1):
    for j in range(1, n):
        if not money[i + j][0] or money[i + j][0] < money[i][0] + coins[i + j]:
            money[i + j][0] = money[i][0] + coins[i + j]
            money[i + j][1] = money[i][1] + [j]

print(money[useless - 1][0])
print(len(money[useless - 1][1]))
output = [1]
for i in money[useless - 1][1]:
    output += [output[-1] + i]
print(*output)
