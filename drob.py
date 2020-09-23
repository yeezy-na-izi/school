def to_10(n, x):
    st = 0
    z = 0
    q = 0
    n = str(n).split('.')
    y = x ** len(n[1])
    for i in range(len(n[1])-1, -1, -1):
        z += int(n[1][i])* x ** st
        st += 1
    st = 0
    for i in range(len(n[0])-1, -1, -1):
        q += int(n[0][i])* x ** st
        st += 1
    number = q + z/y
    print(z, y)
    print(number)
