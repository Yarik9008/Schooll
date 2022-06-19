file = open('C:/Users/Yarik9008/YandexDisk/Schooll/ege/info/probnik/prob-5/17.txt')
data = file.readlines()
data = [int(i[:-1]) for i in data]

massmin103 = []
for i in data:
    if i % 103 == 0:
        massmin103.append(i)

massmin103 = min(massmin103)
print(massmin103)

data1 = data[::1][:-1]
data2 = data[::1][1:]

datain = list(zip(data1, data2))

kol = 0
massoutsum = []

for i in datain:
    if (i[0] + i[1]) % 2 == 0 and abs(i[0] - i[1]) % massmin103  == 0:
        kol += 1
        massoutsum.append((i[0] + i[1]))

print(kol)
print(max(massoutsum))