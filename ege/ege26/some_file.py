sum_a = 0
b = []
x, money = [int(i) for i in input().split()]
for i in range(x):
    inp = input().split()
    if inp[-1] == 'A':
        q = [int(j) for j in inp[:-1]]
        sum_a += q[0] * q[1]
    else:
        q = [int(j) for j in inp[:-1]]
        b.append((q[0], q[1]))

money -= sum_a
kol = 0
b = sorted(b)
for i in b:
    if money < i[0] * i[1]:
        print(money)
        print(i)
        break
    else:
        kol += i[1]
        money -= i[0] * i[1]

print(kol)
