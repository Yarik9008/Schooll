path1 = 'mass/data/92.2.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: x % 2 == 1, ful))
mass2 = list(filter(lambda x: x % 2 == 0, ful))

print(len(mass))
print(len(mass2))


# 13 12 
# 6 9 

# правильно 