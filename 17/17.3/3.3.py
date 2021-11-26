path1 = '17/17.3/data/17-4.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: (int(str(x)[-1]) + int(str(x)[-1]) <= 15) and x % 3 != 0 and x % 4 != 0 and x % 7 !=0, ful))
print(min(mass))
print(sum(mass))

# 1063
# 3858954

# 