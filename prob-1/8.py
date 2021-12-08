from itertools import combinations_with_replacement
mass = list('аворт')
massiv = []
for a in mass:
    for b in mass:
        for c in mass:
            for d in mass:
                massiv.append((a+b+c+d))

print(massiv.index('вата') + 1)