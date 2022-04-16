path1 = '17/17.1/data/17-7.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: str(oct(x))[-1] == '7' and str(oct(x))[-2:]  != '27', ful))
print(mass)
print(len(mass))
print(max(mass))

# 9
# 63

# правильно 