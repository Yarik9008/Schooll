num = 125# число большее по сравнению с исходным на 1 

checkR = True

for i in range(181, 1800):
    if checkR:
        n = str(bin(i))[2:-2]
        n = str(n) + str(sum([int(i) for i in list(str(n))]) % 2)
        n = str(n) + str(sum([int(i) for i in list(str(n))]) % 2)
        q = int(n,2)
        if q >= i:
            print(q)
            break
    else:
        n = str(bin(i))[2:]
        n = str(n) + str(sum([int(i) for i in list(str(n))]) % 2)
        n = str(n) + str(sum([int(i) for i in list(str(n))]) % 2)
        n = int(n, 2)
        if n > num:
            print(i)
            break
