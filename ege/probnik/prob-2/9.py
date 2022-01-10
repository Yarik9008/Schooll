path1 = 'prob-2/9.txt'  # путь до первого файла
mass = [[int(a) for a in i.split('\t')] for i in  open(path1, 'r').readlines()]
kol = 0
for i in mass:
    if (i[0] * i[1] + i[0] * i[2]) < (i[1] * i[2]):
        kol += 1
    elif  (i[1] * i[2] + i[1] * i[0]) < (i[0] * i[2]):
        kol += 1
    elif  (i[0] * i[2] + i[1] * i[2]) < (i[0] * i[1]):
        kol += 1

print(kol)