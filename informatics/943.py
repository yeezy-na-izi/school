triangle = [[1], [1, 1]]
number = int(input())
for i in range(number - 2):
    to_append = [1]
    for j in range(len(triangle[-1]) - 1):
        to_append.append(triangle[-1][j] + triangle[-1][j + 1])
    triangle.append(to_append + [1])
for i in triangle[:number]:
    print(*i)
