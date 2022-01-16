from itertools import product


mass = list('светлана')
check = {}
for i in set(mass):
    check[i] = mass.count(i)
print(check)
massout = list(product(mass, 8))
#print(massout)
kol = 0
for i in set(massout):
    icheck = {}
    for a in set(i):
        icheck[a] = mass.count(a)
    if icheck == check:
        i = ''.join(i)
        if 'aa' not in i:
            kol += 1

print(kol)


