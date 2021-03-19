def hash_num(x):
    q = ''.join([str(ord(i) * ord(i)) for i in list(x)])
    x = ''
    for i in range(len(str(q)) // 2):
        x += str(q)[i * 2:i * 2 + 1]
    return x


list_of_hash = []
x = input()
while x[0] != '#':
    if x[0] == '+':
        list_of_hash.append(hash_num(x[1:]))
    if x[0] == '?':
        if hash_num(x[1:]) in list_of_hash:
            print('YES')
        else:
            print('NO')
    x = input()
