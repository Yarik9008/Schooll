path1 = '17/17.2/data/17-3.txt'

mass = open(path1, 'r').readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

data = list(zip(ful[:-1], ful[1:]))
mass = list(filter(lambda x: sum(x) % 2 == 0 and sum(x) % 10 != 6, data))
otv = list(map(lambda x: sum(x) / 2, mass))

print(len(otv))
print(max(otv))

# 1996
# 9702

#