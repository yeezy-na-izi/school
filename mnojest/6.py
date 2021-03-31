a = input()
print(*[i if a.count(i) == 1 else '' for i in sorted(a)],
      sep='' if [i if a.count(i) == 1 else '' for i in sorted(a)] else 'NO')
