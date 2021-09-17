data = input("Введите постфиксное выражение: ").split()

stack = []
f = 1
i = 0
for x in data:
    if x in "+-*/":
        i += 1
        if len(stack) < 2:
            print("ERROR")
            f = 0
            break
        op2 = int(stack.pop())
        op1 = int(stack.pop())
        if x == "+":
            res = op1 + op2
        elif x == "-":
            res = op1 - op2
        elif x == "*":
            res = op1 * op2
        else:
            res = op1 // op2
        print(f'{i}) {op1} {x} {op2} = {res}')
        stack.append(res)
    else:
        stack.append(x)
if len(stack) == 1:
    print(stack[0])
elif f == 1:
    print("ERROR")
