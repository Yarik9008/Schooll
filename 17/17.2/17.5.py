path1 = '17/17.2/data/17-1.txt'  # путь до первого файла
#path1 = '17/17.2/data/test5.txt'

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

massind = []
for i in range(1, len(ful) - 1):
    if ful[i - 1] < ful[i] and ful[i] > ful[i + 1]:
        massind.append(i) 

mass1 = massind[::1]
mass2 = massind[1:]
data = list(zip(mass1, mass2))

datamin = min(list(map(lambda x: x[1] - x[0], data)))

print(len(massind))
print(datamin)

# 3316
# 2

#
