path1 = '45-71/46.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: x % 2 == 0, ful))
mass2 = list(filter(lambda x: x % 2  == 1, ful))

if len(mass) <= len(mass2):
    print(min(mass))
else:
    print(min(mass2))

# 10
# 84
# 196
# ghfdbkmy
