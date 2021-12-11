file = '26data/26-j5.txt'
with open(file) as input_file:
    useless = input_file.readline()
    all_numbers = [int(i) for i in input_file]
old = all_numbers[::]
for i in range(1, len(all_numbers) - 1):
    all_numbers[i] = sorted([old[i - 1], old[i], old[i + 1]])[1]
output = 0
for i in range(len(all_numbers)):
    if all_numbers[i] < old[i]:
        output += old[i] - all_numbers[i]
print(all_numbers.count(min(all_numbers)), output)
