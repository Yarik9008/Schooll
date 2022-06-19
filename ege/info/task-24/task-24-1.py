file = open('C:/Users/Yarik9008/YandexDisk/Schooll/ege/info/task-24/data/24-1.txt')
s = file.readline()

mass = []
tec = 0
kol_a = 0
for i in range(len(s)):
    sim = s[i]
    if sim == 'E':
        if kol_a >= 3:
            mass.append(tec)
            tec = 0 
            kol_a = 0
        else:
            tec = 0
            kol_a = 0
    elif sim == 'A':
        kol_a += 1
        tec += 1
    else:
        tec += 1

print(max(mass))