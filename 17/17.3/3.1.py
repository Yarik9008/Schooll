path1 = '17/17.3/data/17-4.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: int(str(x)[-2]) <=4 and int(str(x)[-3]) <= 7 and int(str(x)[-3]) >= 3, ful))
print(len(mass))
print(min(mass))

#502
#1305
