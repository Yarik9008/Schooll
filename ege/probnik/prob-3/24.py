from tabnanny import check


path1 = 'ege/probnik/prob-3/data/24.txt'  # путь до первого файла

fil = open(path1, 'r')
lines = list(fil.readline())

kol_F = 0
check_e = False
kol = 0
for i in lines:
    if i == 'E':
        if check_e:
            if kol_F > 12:
                kol += 1
        check_e = not check_e
        kol_F = 0
    elif i == 'F':
        if check_e:
            kol_F +=1
   


print(kol)
    
        
