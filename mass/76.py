path1 = 'schooll/mass/data/76.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

# нахождение кол-во пар 
mass1 = ful[:-1]
mass2 = ful[1:]
data = list(zip(mass1, mass2))
massdata = list(filter(lambda x: (x[0] - x[1]) % 7 != 0, data))
massdata = [list(a) for a in massdata]
l = len(massdata) # кол-во пар 
print(l)

# 256
# 71
# 156

# правильно 