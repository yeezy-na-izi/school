with open('26data/26-j8.txt') as input_file:
    useless = input_file.readline()
    all_numbers = [int(i) for i in input_file]
    all_numbers.sort()
print(sum(all_numbers[:int(len(all_numbers) * 0.7)]) * 0.7 + sum(all_numbers[int(len(all_numbers) * 0.7):]) * 0.6)
print(sum(all_numbers[:len(all_numbers) // 2]) * 0.6 + sum(all_numbers[len(all_numbers) // 2:]) * 0.65)
print(all_numbers[-1] * 0.6)
print(3309103.8999999994 - 3245311.25)
