path1 = 'schooll/mass/data/41.3.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass1 = ful[:-1]
mass2 = ful[1:]

data = list(zip(mass1, mass2))
massdata = list(filter(lambda x: sum(x) > 0 and x[0] * x[1] % 2 == 1, data))


print(len(massdata))

# 8 
# 25
# 12

#  не правильно 