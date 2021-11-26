x = int(input())
count = 0
matrix = []
for i in range(x):
    string = [int(i) for i in input().split()]
    count += sum(string[i + 1:])
    matrix.append(string)


def in_deep(position):
    for index, element in enumerate(matrix[position]):
        if element and index not in output:
            output.add(index)
            in_deep(index)


output = {0}
in_deep(0)
print('YES' if count + 1 == x and len(output) == x else 'NO')
