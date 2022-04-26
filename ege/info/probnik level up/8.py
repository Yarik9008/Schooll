from itertools import combinations_with_replacement
stroka = sorted(list('степуха'))
mass = []
for q in stroka:
    for w in stroka:
        for e in stroka:
            for r in stroka:
                mass.append((q,w,e,r))

kol = 0
for i in mass[999:]:
    if len(set(i)) == 1:
        kol += 1

print(kol)

# 4