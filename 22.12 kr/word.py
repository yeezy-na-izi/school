alph = set("вор0та")
n = 0
for a1 in alph:
    for a2 in alph - set(a1):
        for a3 in alph - set(a1 + a2):
            for a4 in alph - set(a1 + a2 + a3):
                for a5 in alph - set(a1 + a2 + a3 + a4):
                    a = a1 + a2 + a3 + a4 + a5
                    if "о0" not in a and "0о" not in a and "оа" not in a and "ао" not in a and "аи" not in a and "иа" not in a:
                        n += 1

print(n)