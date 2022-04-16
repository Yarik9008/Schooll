path1 = 'kontroll/data/КР5-5.txt'

mass = open(path1, 'r').readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

#print('input: ', *ful)

min3 = min(list(filter(lambda x: x % 3 == 0, ful)))
min5 = min(list(filter(lambda x: x % 5 == 0, ful)))

for i in range(len(ful)):
    if ful[i] % 15 == 0:
        ful[i]  -= min3 + min5
    elif ful[i] % 5 == 0:
        ful[i] -= min5
    elif ful[i] % 3 ==0:
        ful[i] -= min3

print('out: ', *ful) 

#