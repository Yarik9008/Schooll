from itertools import combinations_with_replacement


mass = list('светлана')
check = {}
for i in set(mass):
    check[i] = mass.count(i)
print(check)
massout = list(combinations_with_replacement(mass, 8))
kol = 0
for i in set(massout):
    icheck = {}
    for a in set(i):
        icheck[a] = mass.count(a)
    if icheck == check:
        i = ''.join(i)
        if i not in 'aa':
            kol += 1

print(kol)


