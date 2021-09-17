input()
x = [int(i) for i in input().split()]
input()
for i in input().split():
    x[int(i) - 1] -= 1
print(*['no' if i >= 0 else 'yes' for i in x], sep='\n')
