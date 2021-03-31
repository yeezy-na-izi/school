a = input()[:-1].split(',')

a = ''.join(a[::2])
a = set(a)
x = set('бвгджзлмнр')
a = x - (x - a)
print(*sorted(a))
