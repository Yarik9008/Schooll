path1 = '45-71/58.1.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: len(str(hex(x))) == 4 and str(hex(x))[-2] > str(hex(x))[-1], ful))
print(min(mass))

# 48
# 33
# 112

