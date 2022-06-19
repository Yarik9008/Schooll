file = open('C:/Users/Yarik9008/YandexDisk/Schooll/ege/info/probnik/prob-5/9.txt')
data = file.readlines()
kol = 0
for i in data:
    mass = list(map(lambda x: float(x), i[:-1].split('\t')))
    sr = (max(mass) + min(mass)) / 2
    if sr in mass:
        kol += 1

print(kol)
