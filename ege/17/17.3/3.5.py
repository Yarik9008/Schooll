path1 = '17/17.3/data/17-6.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass1 = ful[::1]
mass2 = ful[1:]
mass3 = ful[2:]

data = list(zip(mass1,mass2, mass3))

masss = list(filter(lambda x: str(bin(x[0])).count('1') == 3 and   str(bin(x[1])).count('1') == 3  and   str(bin(x[2])).count('1') == 3, data))

massOut = list(map(lambda x: sum(x), masss))

print(len(massOut))
print(max(massOut))

# 16
# 305

# 