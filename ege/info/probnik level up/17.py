path1 = 'C:/Users/Yarik9008/YandexDisk/Schooll/ege/info/probnik level up/17.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readlines()
ful = [int(a[:-1]) for a in mass[:-1]]
ful.append(int(mass[-1]))
print(len(ful))
suma = 0
for i in ful:
    suma += int(str(abs(i))[0])


mass1 = ful[:-1]
mass2 = ful[1:]
data = list(zip(mass1, mass2))

kol = 0
for i in data:
    if i[0] * i[1]  > suma:
        kol += 1

print(kol)
#print(data)