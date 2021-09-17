a, b, c = int(input()), int(input()), int(input())
if input() == '1':
    q = min(a, b)
    if q >= c:
        print(1 + q - c)
    else:
        print(max(a, b) - c + 1)
else:
    if min(a, b) >= c:
        print(max(a, b) - min(a, b) + c)
    else:
        print(c - 1)
