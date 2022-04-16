path1 = 'kontroll/data/КР5-4.txt'

mass = open(path1, 'r').readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

#print('input: ', *ful)

massi = list(filter(lambda x: x % 2 == 0, ful))

mini = min(massi)

if mini <= 20:
    pl = 20 - mini
    print(pl)
    for i in range(len(ful)):
        if ful[i] % 2 == 0:
            ful[i] += pl
else:
    mi = mini - 20
    print(mi)
    for i in range(len(ful)):
        if ful[i] % 2 == 0:
            ful[i] -= mi

print(f'out: ', *ful)

# правильно
