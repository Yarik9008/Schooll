path1 = 'prob-1/data/17-test.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass1 = ful[:-1]
mass2 = ful[1:]

data = list(zip(mass1, mass2))

massotv = list(filter(lambda x: sum(x) % 5 == 0 and (x[0]% 3 == 0 or x[1] % 3 == 0), data))
maxi = max(list(map(lambda x: sum(x), massotv)))

print(len(massotv))
print(maxi)

# 635
# 19730
