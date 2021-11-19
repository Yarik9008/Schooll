path1 = 'schooll/17/17_файлы/17-4.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))

otv = []
for i in ful:
    if i % 13 == 7 and (i % 7 != 0 and i % 11 != 0):
        otv.append(i)

print(len(otv))
print(max(otv) - min(otv))

# 126
# 8515