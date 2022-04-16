from tabnanny import check



def f(n):
    bini = str(bin(n)[2:])
    kol_1 = 0
    kol_0 = 0 
    check = False 
    for i in bini:
        if check:
            if i == '1':
                kol_1 += 1
        else:
            if i == '0':
                kol_0 += 1
        check = not check

    return kol_1 - kol_0

for i in range(10000000):
    if f(i) == 5:
        print(i)
        break

