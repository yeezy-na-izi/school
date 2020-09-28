def to_10(n, x):
    st = 1
    z = 0
    q = 0
    n = str(n).split('.')
    y = x ** len(n[1])
    for i in range(len(n[1])-1, -1, -1):
        if n[1][i].isdigit():            
            z += int(n[1][i])* x * st
        else:
            z += (ord(n[1][i]) - 55) * x * st
        st *= x
    st = 1
    for i in range(len(n[0])-1, -1, -1):
        if n[0][i].isdigit():            
            q += int(n[0][i])* x * st
        else:
            q += (ord(n[0][i]) - 55) * x * st
        st *= x
    number = q + z/y
    print(z, y)
    print(number)
