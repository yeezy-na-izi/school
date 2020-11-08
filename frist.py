stack = []
c = []
while True:
    a = input().split()
    if a[0] == "push":
        stack.append(a[1])
        c.append("ok")
    elif a[0] == "size":
        c.append(len(stack))
    elif a[0] == "clear":
        stack.clear()
        c.append('ok')
    elif a[0] == "pop":
        if len(stack) > 0:
            c.append(stack.pop(0))
        else:
            c.append('error')
    elif a[0] == "front":
        if len(stack) > 0:
            c.append(stack[0])
        else:
            c.append('error')
    elif a[0] == "exit":
        c.append("bye")
        break
    else:
        c.append('error')
for i in range(len(c)):
    print(c[i])
