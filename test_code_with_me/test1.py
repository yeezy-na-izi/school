x = list('апорт')
counter = 0
for a1 in x:
    for a2 in x:
        for a3 in x:
            for a4 in x:
                for a5 in x:
                    word = a1 + a2 + a3 + a4 + a5
                    if (set(x) == set(word)) and ('ао' not in word) and ('оа' not in word):
                        counter += 1
print(counter)