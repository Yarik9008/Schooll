path1 = '17/17.2/data/17-1.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass1 = ful[:-1]
mass2 = ful[1:]

data = list(zip(mass1, mass2))

mass = list(filter(lambda x: (x[0] % 9 == 0 and str(oct(x[1]))[-1] == '3' ) or (x[1] % 9 == 0 and str(oct(x[0]))[-1] == '3' ), data))

otv = list(map(lambda x: sum(x), mass))

massiv = []
for i in mass:
    massiv.append(i[0])
    massiv.append(i[1])

print(len(otv))
print(max(massiv))

# 275
# 9972

# правильно 

