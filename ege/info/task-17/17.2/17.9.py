path1 = '17/17.2/data/17-3.txt'

mass = open(path1, 'r').readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

data = list(zip(ful[:-1], ful[1:]))
mass = list(filter(lambda x: sum(x) % 7 == 0 and x[0] * x[1] > 0, data))
otv = min(list(map(lambda x: x[0] * x[1], mass)))

print(len(mass))
print(otv)

# 359
# 115022

#

