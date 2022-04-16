# перевод числа n в бинарку 
# сумма всего и остаток в конец
# сумма всего и остаток в конец
# перевод из двоичной в десятичную 
param = 86


for i in range(1,12000000):
    bini = bin(i)[2:]
    bini = str(bini) + str(sum([int(s) for s in list(str(bini))]) % 2)
    bini = str(bini) + str(sum([int(s) for s in list(str(bini))]) % 2)
    num = int(bini, 2)
    if num > param:
        print(num)
        break
