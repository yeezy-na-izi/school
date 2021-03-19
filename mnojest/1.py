x = int(input()) + int(input())
y = set()
for i in range(x):
    y.add(input())
print(len(y) * 2 - x if len(y) * 2 - x else 'NO')
