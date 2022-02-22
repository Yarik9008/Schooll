
path1 = 'ege/probnik/prob-3/data/17.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass1 = ful[:-1]
mass2 = ful[1:]

data = list(zip(mass1, mass2))

sr = 0
kol = 0
check_sj = False
for i in ful:
    if check_sj:
        sr += i
        kol += 1
    check_sj = not check_sj
sr = sr / kol 

mass_out = []
for i in data:
    if (i[0] % 7 == 0 and i[1] < sr) or (i[1] % 7 == 0 and i[0] < sr):
        mass_out.append(i)

print(len(mass_out))

otv = list(map(lambda x: sum(x), mass_out))
print(max(otv))