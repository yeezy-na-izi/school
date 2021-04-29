def gsd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
q = 0
while x1 * y2 < x2 * y1:
    x1 += 1
    y1 += 1
    gcd_n = gsd(x1, y1)
    x1 //= gcd_n
    y1 //= gcd_n
    q += 1
if x1 == x2 and y1 == y2:
    print(q)
else:
    print(0)


