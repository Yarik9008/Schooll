from itertools import combinations

path = 'C:/Users/Yarik9008/YandexDisk/Schooll/ege/info/probnik-2/data-9.txt'

fil = open(path, 'r')
mass = fil.readlines()
mass = [[int(i)for i in a[:-2].split('\t')] for a in mass]
kol = 0 
for data in mass:
    fulldata = [sum(s) for s in list(combinations(data, 3))]
    for i in fulldata:
        if i % 2 == 0:
            
            kol += 1 
            break
print(kol)