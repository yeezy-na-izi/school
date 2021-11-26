count_point, amount = [int(i) for i in input().split()]
all_ways = [{i} for i in range(count_point)]

for i in range(amount):
    numbers = [int(i) - 1 for i in input().split()]
    way_for_numbers = all_ways[numbers[0]] | all_ways[numbers[1]]
    for element in list(way_for_numbers):
        all_ways[element] = way_for_numbers

output = set(tuple(i) for i in all_ways)
print(len(output))
for i in list(output):
    print(len(i))
    print(*[j + 1 for j in i])

# 6 4
# 4 2
# 1 4
# 6 4
# 3 6
