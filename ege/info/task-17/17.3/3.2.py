path1 = '17/17.3/data/17-4.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: x % 9 != 0 and sum([int(i) for i in list(str(x))]) % 5 == 0, ful))

print(max(mass))
print(len(mass))

# 9727
# 388

#