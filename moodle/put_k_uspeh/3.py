data = [[] for i in range(120)]
with open('file_b.txt') as input_file:
    for i in range(int(input_file.readline())):
        number = int(input_file.readline())
        data[number % 120].append((number, i))
output = []
for i in range(1, 60):
    for j in data[i]:
        for q in data[120 - i]:
            if (j[0] > q[0] and j[1] < q[1]) or (j[0] < q[0] and j[1] > q[1]):
                output.append([j, q])
print(max(output, key=lambda x: x[0][0] + x[1][0]))