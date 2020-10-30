import time

a, b = int(input()), int(input())
z = time.time()
c21 = 0
c12 = 0
while a > 0 and b > 0:
    a -= 1
    b -= 1
    if a >= b:
        c21 += 1
        a -= 1
    else:
        c12 += 1
        b -= 1
if a != b:
    print(-1)
else:
    print(c21, c12)
print(time.time() - z)
