n = int(input())
a = set()
for i in range(n):
    a.add(int(input()))
s = set()
for i in a:
    if i % 2 == 0:
        for j in str(i):
            s.add(int(j))
print(*(sorted(s)))