path1 = '17/17.2/data/17-3.txt'

mass = open(path1, 'r').readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

data = list(zip(ful[:-1], ful[1:]))
otv = []

for a in data:
    if (a[0] % 2 != 0 and a[1] % 0 == 0) or (a[0] % 2 == 0 and a[1] % 2 != 0):
        if 