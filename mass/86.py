path1 = 'schooll/mass/data/76.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))


mass = list(filter(lambda x: x > 9 and x < 100 and (int(str(x)[0] + int(str(x)[0]))) == 5, ful))

print(len(mass))