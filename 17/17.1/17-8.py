path1 = '17/17.1/data/17-5.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass1 = ful[:-1]
mass2 = ful[1:]

data = list(zip(mass1, mass2))

mass = list(filter(lambda x: x[0] % 10 == 5 and x[1] % 10 == 5, data))

otv = list(map(lambda x: sum(x), mass))

print(len(otv))
print(max(otv))

# 1
# 40

# правильно 