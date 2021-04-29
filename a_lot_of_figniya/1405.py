a, b, c = input().replace('+', ' ').replace('=', ' ').split()
x = 1
a1 = 0
b1 = 0
c1 = 1
while a1 + b1 != c1 and x < 37:
    try:
        a1 = int(a, x)
        b1 = int(b, x)
        c1 = int(c, x)
    except:
        pass
    x += 1
if x != 37:
    print(x - 1)
else:
    print(-1)
