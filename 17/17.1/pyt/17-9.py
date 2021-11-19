path1 = 'schooll/17/17_файлы/17-7.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

mass = list(filter(lambda x: str(hex(x))[-1] == '7' and str(hex(x))[-2:]  != '27', ful))

print(len(mass))
print(max(mass))

# 4
# 87