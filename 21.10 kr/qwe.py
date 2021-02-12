output_file = open('out.txt', 'w')
for i in range(1, 1000000):
    if not i % 3:
        print('Fizz', end='', file=output_file)
        if not i % 5:
            print('Buzz', file=output_file)
    elif not i % 5:
        print('Fizz', file=output_file)
    else:
        print(i, file=output_file)
output_file.close()
