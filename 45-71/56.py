path1 = '45-71/56.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x : len(str(hex(x))) - 2 >= 3 and str(hex(x))[-1] == 'c', ful))

if len(mass) > 0:
    print(min(mass))
else:
    print(0)

# 780
# 1132
# 556