n, k = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append(int(input()))
left = min(a) // k
right = sum(a) // k + 1
while right > left + 1:
    m = (left + right) // 2
    if k > sum(i // m for i in a):
        right = m
    else:
        left = m
print(left)
