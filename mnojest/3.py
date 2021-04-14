x = int(input())
y = int(input())
qwe = set()
for i in range(x):
    qwe.add(input())
for i in range(y):
    print('YES' if input() in qwe else 'NO')
