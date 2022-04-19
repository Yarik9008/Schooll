path1 = 'ege/info/probnik-2/файлы/17.txt'

mass = open(path1, 'r').readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

data = list(zip(ful[:-1], ful[1:]))
print(len(data))

data = list(filter(lambda x: (x[0] % 5 == 0 and x[1] % 5  != 0) or (x[0] % 5 != 0 and x[1] % 5  == 0), data))
data = list(filter(lambda x: abs(x[0] - x[1]), data))

print(len(data))
