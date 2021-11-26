x = int(input())
matrix = []
output = set()


def in_deep(position):
    for index, element in enumerate(matrix[position]):
        if element and index not in output:
            output.add(index)
            in_deep(index)


for i in range(x):
    matrix.append([int(i) for i in input().split()])
out = []
q = []
for i in range(x):
    if i not in q:
        output = {i}
        in_deep(i)
        out += [list(output)]
        q += list(output)
print(len(out))
for i in out:
    print(len(i))
    print(*[j + 1 for j in sorted(i)])
