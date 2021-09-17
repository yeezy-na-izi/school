n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
left = 0
right = a[-1] - a[0] + 1
while left < right:
    mid = (left + right) // 2
    cows = 1
    last = a[0]
    for i in a[1:]:
        if i - last > mid:
            cows += 1
            last = i
    if cows >= k:
        left = mid + 1
    else:
        right = mid
print(left)
