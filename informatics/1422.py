a, b = [int(i) for i in input().split()]
x = a
y = b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(int(x / (a + b) * y))