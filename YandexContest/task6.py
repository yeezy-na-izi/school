count, length = [int(i) for i in input().split()]
stack = []
counter = 1
output = []
for i in range(count):
    name, number = input().split()
    number = int(number)
    check_time = list(filter(lambda x: x[1] < number, stack)) or len(stack) < length
    if check_time:
        stack_in = list(filter(lambda x: x[0] == name, stack))
        if stack_in:
            output.append(f'{counter} UPDATE {name}')
            stack[stack.index(stack_in[0])] = (name, number)
        else:
            if len(stack) == length:
                output.append(f'{counter} DELETE {stack.pop(stack.index(min(stack, key=lambda x: x[1])))[0]}')
            output.append(f'{counter} PUT {name}')
            stack.append((name, number))
        counter += 1
print('\n'.join(output))
