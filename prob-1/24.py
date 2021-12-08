path1 = 'prob-1/data/24.txt'  # путь до первого файла

fil = open(path1, 'r')
mass = fil.readline()

maxkol = 0
kol = 0
kola = False
for i in mass:
    if i == 'A':
        if kola:
            if kol > maxkol:
                maxkol = kol
                kol = 0 
            else:
                kol = 0
        else:
            kola = True
            kol += 1
    else:
        kol += 1

print(maxkol)