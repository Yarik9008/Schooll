from math import fabs


path1 = '17/17.2/data/17-1.txt'  # путь до первого файла
fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass1 = ful[::1]
mass2 = ful[1:]
data = list(zip(mass1, mass2))

kol = 0 
for i in range(len(ful)):
    if i == 0:
        continue
    if ful[i-1] < ful[i]: 
        kol += 1 

minraz = min(list(map(lambda x: fabs(x[0] - x[1]), data)))

print(kol)
print(minraz)

# 5012
# 5

#