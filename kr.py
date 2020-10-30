import math

st = input().split()
stack = []
F = False
for i in st:
    if i.isdigit():
        stack.append(i)
    else:
        if len(stack) > 1 and i in '+-/*':
            x1 = stack.pop()
            x2 = stack.pop()
            stack.append(eval(f'{x2}{i}{x1}'))
        elif len(stack) > 0 and i not in '+-/*':
            if i == 'abs':
                z = compile(f'{i}({stack.pop()})', "<string>", "eval")
            else:
                z = compile(f'math.{i}({stack.pop()})', "<string>", "eval")
            stack.append(eval(z))
        else:
            F = True
            break
if F or len(stack) != 1:
    print('ERROR')
else:
    print("{0:.3f}".format(stack[0]))
