path1 = '17/17.2/17-1.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass1 = ful[:-1]
mass2 = ful[1:]

data = list(zip(mass1, mass2))

mass = list(filter(lambda x: (x[0] % 7 == 0 and x[1] % 17 != 0) or (x[1] % 7 == 0 and x[0] % 17 != 0), data))

otv = list(map(lambda x: sum(x), mass))

massiv = []
for i in mass:
    massiv.append(i[0])
    massiv.append(i[1])

print(len(otv))


# 2510
# 19632

#  правильно 
