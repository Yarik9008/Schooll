path1 = '45-71/71.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: x % 2 == 0, ful))
mass2 = list(filter(lambda x: x % 2  == 1, ful))

if max(mass) < max(mass2):
    for i in range(len(ful)):
        if ful[i] % 2 == 0:
            ful[i] = 0
else:
    for i in range(len(ful)):
        if ful[i] % 2 == 1:
            ful[i] = 0

print(ful)
print(max(mass))
print(max(mass2))

# 9940 9875
# 920 895
# 1498 1497 