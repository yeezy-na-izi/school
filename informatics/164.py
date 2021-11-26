def in_deep(position):
    for index, element in enumerate(matrix[position]):
        if element and index not in output:
            output.add(index)
            in_deep(index)


# 0 1 1
# 1 0 1
count, start_pos = [int(i) for i in input().split()]
matrix = []
out = []
for i in range(count):
    matrix.append([int(i) for i in input().split()])

output = {start_pos - 1}

in_deep(position=start_pos - 1)
print(len(output))
print(out)
