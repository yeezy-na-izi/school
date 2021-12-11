with open('26data/26-j7.txt') as input_file:
    useless = input_file.readline()
    all_numbers = [int(i) for i in input_file]
    all_numbers.sort(reverse=True)
all_sum = sum(all_numbers) * 0.6
rich_sum = sum(all_numbers[:len(all_numbers) // 5]) * 0.8
print(rich_sum, (all_sum - rich_sum) / sum(all_numbers[len(all_numbers) // 5:]) * all_numbers[-1])
