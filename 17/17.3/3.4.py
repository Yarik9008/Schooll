path1 = '17/17.3/data/17-4.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: str(x).count('0') >= 2 and x % 7 == 0, ful))

print(max(mass))
print(len(mass))

# 9009
# 10 